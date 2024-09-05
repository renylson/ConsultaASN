from flask import Flask, request, render_template, send_from_directory
import requests
import socket
import re
from urllib.parse import urlparse
import os

app = Flask(__name__)

API_KEY = 'XXXXXXXXXXXX'  # Seu token da API IPinfo

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

def get_ip_info(ip):
    url = f'https://ipinfo.io/{ip}/json?token={API_KEY}'
    response = requests.get(url)
    return response.json()

def extract_ip_from_cidr(cidr):
    return cidr.split('/')[0]

def resolve_domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.error as e:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form.get('ips')
        items = [item.strip() for item in input_data.split(',')]
        results = []

        for item in items:
            parsed_url = urlparse(item)
            domain = parsed_url.netloc or parsed_url.path
            if re.match(r'^[a-zA-Z0-9.-]+$', domain):
                ip = resolve_domain_to_ip(domain)
                if ip:
                    print(f"Resolvendo domínio {domain} para IP {ip}")
                else:
                    results.append({"error": f"Não foi possível resolver o domínio {domain}."})
                    continue
            else:
                ip = extract_ip_from_cidr(item)

            try:
                info = get_ip_info(ip)
                results.append(info)
            except Exception as e:
                results.append({"error": str(e)})

        return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

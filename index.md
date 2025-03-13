<div class="hero-section">
  <div class="hero-background">
    <div class="hero-gradient"></div>
    <div class="hero-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
      <div class="particles-container" id="particles-js"></div>
    </div>
  </div>
  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title animate-title">Claude<span class="text-accent">実践</span>ラボ</h1>
      <p class="hero-description animate-fade-up">ビジネスと開発のプロフェッショナルのためのAI活用プラットフォーム</p>
      <div class="hero-buttons animate-fade-up-delay">
        <a href="{{ site.baseurl }}/categories/" class="btn btn-primary btn-lg"><i class="fas fa-layer-group"></i> ソリューション一覧</a>
      </div>
    </div>
  </div>
  <div class="scroll-indicator">
    <div class="mouse">
      <div class="wheel"></div>
    </div>
    <div class="arrow-scroll-down">
      <span></span>
      <span></span>
      <span></span>
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>

<style>
/* スマートなFVアニメーション */
.hero-section {
  position: relative;
  height: 100vh;
  min-height: 650px;
  max-height: 900px;
  display: flex;
  align-items: center;
  overflow: hidden;
  margin-top: -80px;
  padding-top: 80px;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #f8fafc;
  overflow: hidden;
  z-index: -1;
}

.hero-gradient {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.08), rgba(58, 12, 163, 0.12));
  z-index: 0;
}

.particles-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
}

.hero-shapes {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0;
  animation-fill-mode: forwards;
}

.shape-1 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(67, 97, 238, 0.08) 0%, rgba(67, 97, 238, 0) 70%);
  top: -150px;
  right: -100px;
  animation: float 15s ease-in-out infinite, fadeIn 1.5s ease forwards 0.2s;
}

.shape-2 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(72, 149, 239, 0.08) 0%, rgba(72, 149, 239, 0) 70%);
  bottom: -50px;
  left: -100px;
  animation: float 18s ease-in-out infinite reverse, fadeIn 1.5s ease forwards 0.5s;
}

.shape-3 {
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(58, 12, 163, 0.05) 0%, rgba(58, 12, 163, 0) 70%);
  bottom: -200px;
  right: 15%;
  animation: float 20s ease-in-out infinite, fadeIn 1.5s ease forwards 0.8s;
}

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
  100% { transform: translateY(0) rotate(0deg); }
}

@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

.hero-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 10;
}

.animate-title {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 1s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
}

.animate-fade-up {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 1s cubic-bezier(0.215, 0.61, 0.355, 1) forwards 0.3s;
}

.animate-fade-up-delay {
  opacity: 0;
  transform: translateY(30px);
  animation: fadeUp 1s cubic-bezier(0.215, 0.61, 0.355, 1) forwards 0.6s;
}

@keyframes fadeUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-title {
  font-size: 5.5rem;
  font-weight: 900;
  margin-bottom: 1.5rem;
  background: linear-gradient(to right, #1e40af, #3b82f6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
  line-height: 1.1;
  letter-spacing: -0.03em;
  position: relative;
  display: inline-block;
}

.hero-title::after {
  content: "";
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 0;
  height: 4px;
  background: linear-gradient(to right, #4361ee, #3a0ca3);
  border-radius: 2px;
  animation: lineExpand 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) forwards 1s;
}

@keyframes lineExpand {
  from { width: 0; }
  to { width: 120px; }
}

.text-accent {
  color: #3a0ca3;
  -webkit-text-fill-color: #3a0ca3;
  text-fill-color: #3a0ca3;
}

.hero-description {
  font-size: 1.5rem;
  color: var(--medium-text);
  margin-bottom: 3rem;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.5;
}

.hero-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-bottom: 2rem;
}

.btn-lg {
  padding: 15px 36px;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 30px;
  min-width: 220px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  overflow: hidden;
  position: relative;
  z-index: 1;
}

.btn-primary {
  background: linear-gradient(45deg, #4361ee, #3a0ca3);
  border: none;
  box-shadow: 0 10px 25px rgba(67, 97, 238, 0.3);
  transition: all 0.3s ease;
}

.btn-primary::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg, #3a0ca3, #4361ee);
  transition: all 0.4s ease;
  z-index: -1;
}

.btn-primary:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(67, 97, 238, 0.4);
}

.btn-primary:hover::after {
  left: 0;
}

/* スクロールインジケーター */
.scroll-indicator {
  position: absolute;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  display: flex;
  flex-direction: column;
  align-items: center;
  opacity: 0;
  animation: fadeIn 1s ease forwards 1.5s;
}

.mouse {
  width: 30px;
  height: 50px;
  border: 2px solid rgba(67, 97, 238, 0.6);
  border-radius: 20px;
  display: flex;
  justify-content: center;
  padding-top: 10px;
  margin-bottom: 10px;
}

.wheel {
  width: 4px;
  height: 8px;
  background-color: rgba(67, 97, 238, 0.8);
  border-radius: 2px;
  animation: scroll 1.5s ease infinite;
}

@keyframes scroll {
  0% { transform: translateY(0); opacity: 1; }
  50% { transform: translateY(10px); opacity: 0.5; }
  100% { transform: translateY(0); opacity: 1; }
}

.arrow-scroll-down {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.arrow-scroll-down span {
  display: block;
  width: 10px;
  height: 10px;
  border-bottom: 2px solid rgba(67, 97, 238, 0.6);
  border-right: 2px solid rgba(67, 97, 238, 0.6);
  transform: rotate(45deg);
  margin: -6px 0;
  animation: scrollDown 1.5s infinite;
}

.arrow-scroll-down span:nth-child(2) {
  animation-delay: 0.2s;
}

.arrow-scroll-down span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes scrollDown {
  0% { opacity: 0; transform: rotate(45deg) translate(-6px, -6px); }
  50% { opacity: 1; }
  100% { opacity: 0; transform: rotate(45deg) translate(6px, 6px); }
}

/* Particles.js 用の初期化 */
document.addEventListener("DOMContentLoaded", function() {
  particlesJS("particles-js", {
    "particles": {
      "number": {
        "value": 50,
        "density": {
          "enable": true,
          "value_area": 800
        }
      },
      "color": {
        "value": "#4361ee"
      },
      "shape": {
        "type": "circle",
        "stroke": {
          "width": 0,
          "color": "#000000"
        },
        "polygon": {
          "nb_sides": 5
        }
      },
      "opacity": {
        "value": 0.2,
        "random": true,
        "anim": {
          "enable": true,
          "speed": 1,
          "opacity_min": 0.1,
          "sync": false
        }
      },
      "size": {
        "value": 3,
        "random": true,
        "anim": {
          "enable": true,
          "speed": 2,
          "size_min": 0.3,
          "sync": false
        }
      },
      "line_linked": {
        "enable": true,
        "distance": 150,
        "color": "#4361ee",
        "opacity": 0.15,
        "width": 1
      },
      "move": {
        "enable": true,
        "speed": 1,
        "direction": "none",
        "random": true,
        "straight": false,
        "out_mode": "out",
        "bounce": false,
        "attract": {
          "enable": false,
          "rotateX": 600,
          "rotateY": 1200
        }
      }
    },
    "interactivity": {
      "detect_on": "canvas",
      "events": {
        "onhover": {
          "enable": true,
          "mode": "grab"
        },
        "onclick": {
          "enable": true,
          "mode": "push"
        },
        "resize": true
      },
      "modes": {
        "grab": {
          "distance": 140,
          "line_linked": {
            "opacity": 0.4
          }
        },
        "bubble": {
          "distance": 400,
          "size": 40,
          "duration": 2,
          "opacity": 8,
          "speed": 3
        },
        "repulse": {
          "distance": 200,
          "duration": 0.4
        },
        "push": {
          "particles_nb": 4
        },
        "remove": {
          "particles_nb": 2
        }
      }
    },
    "retina_detect": true
  });
});

/* レスポンシブ調整 */
@media (max-width: 992px) {
  .hero-title {
    font-size: 4.5rem;
  }
  
  .hero-description {
    font-size: 1.3rem;
  }
  
  .scroll-indicator {
    bottom: 20px;
  }
}

@media (max-width: 768px) {
  .hero-section {
    height: 85vh;
    min-height: 550px;
  }
  
  .hero-title {
    font-size: 3.8rem;
  }
  
  .hero-description {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .scroll-indicator {
    bottom: 15px;
  }
  
  .mouse {
    width: 25px;
    height: 40px;
  }
}

@media (max-width: 576px) {
  .hero-section {
    height: 80vh;
    min-height: 500px;
  }
  
  .hero-title {
    font-size: 3rem;
  }
  
  .hero-title::after {
    width: 80px;
    height: 3px;
    bottom: -10px;
  }
  
  .hero-description {
    font-size: 1.1rem;
  }
  
  .btn-lg {
    padding: 12px 30px;
    font-size: 1rem;
    min-width: 200px;
  }
  
  .scroll-indicator {
    display: none;
  }
}
</style>

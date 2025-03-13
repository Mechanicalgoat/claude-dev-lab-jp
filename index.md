---
layout: default
title: ホーム
---

<div class="hero-section">
  <div class="hero-background">
    <div class="hero-gradient"></div>
    <div class="hero-shapes">
      <div class="shape shape-1"></div>
      <div class="shape shape-2"></div>
      <div class="shape shape-3"></div>
    </div>
  </div>
  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title">Claude<span class="text-accent">実践</span>ラボ</h1>
      <p class="hero-description">ビジネスと開発のプロフェッショナルのためのAI活用プラットフォーム</p>
      <div class="hero-buttons">
        <a href="{{ site.baseurl }}/categories/" class="btn btn-primary btn-lg"><i class="fas fa-th-large"></i> ソリューション一覧</a>
        <a href="{{ site.baseurl }}/about/" class="btn btn-outline btn-lg"><i class="fas fa-info-circle"></i> 詳細を確認</a>
      </div>
    </div>
  </div>
</div>

<style>
/* FVとヘッダーの強化 */
.site-header {
  background-color: transparent;
  box-shadow: none;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  border-bottom: none;
}

.site-header.scrolled {
  background-color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(226, 232, 240, 0.7);
}

.site-logo {
  background: linear-gradient(135deg, #4361ee, #3a0ca3);
}

.hero-section {
  position: relative;
  height: 85vh;
  min-height: 600px;
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
  background: linear-gradient(135deg, rgba(67, 97, 238, 0.1), rgba(58, 12, 163, 0.15));
  z-index: 0;
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
}

.shape-1 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(67, 97, 238, 0.08) 0%, rgba(67, 97, 238, 0) 70%);
  top: -150px;
  right: -100px;
  animation: float 15s ease-in-out infinite;
}

.shape-2 {
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(72, 149, 239, 0.08) 0%, rgba(72, 149, 239, 0) 70%);
  bottom: -50px;
  left: -100px;
  animation: float 18s ease-in-out infinite reverse;
}

.shape-3 {
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(58, 12, 163, 0.05) 0%, rgba(58, 12, 163, 0) 70%);
  bottom: -200px;
  right: 15%;
  animation: float 20s ease-in-out infinite;
}

@keyframes float {
  0% { transform: translateY(0) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
  100% { transform: translateY(0) rotate(0deg); }
}

.hero-content {
  text-align: center;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
  z-index: 10;
}

.hero-title {
  font-size: 5rem;
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
  width: 100px;
  height: 4px;
  background: linear-gradient(to right, #4361ee, #3a0ca3);
  border-radius: 2px;
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
  padding: 15px 30px;
  font-size: 1.1rem;
  font-weight: 600;
  border-radius: 8px;
  min-width: 200px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.btn-primary {
  background: linear-gradient(to right, #4361ee, #3a0ca3);
  border: none;
  box-shadow: 0 10px 25px rgba(67, 97, 238, 0.3);
  transition: all 0.3s ease;
}

.btn-primary:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(67, 97, 238, 0.4);
}

.btn-outline {
  background-color: transparent;
  border: 2px solid #4361ee;
  color: #4361ee;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background-color: rgba(67, 97, 238, 0.1);
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(67, 97, 238, 0.1);
}

/* レスポンシブ対応 */
@media (max-width: 992px) {
  .hero-title {
    font-size: 4rem;
  }
  
  .hero-description {
    font-size: 1.3rem;
  }
}

@media (max-width: 768px) {
  .hero-section {
    height: 70vh;
    min-height: 500px;
  }
  
  .hero-title {
    font-size: 3rem;
  }
  
  .hero-description {
    font-size: 1.2rem;
    margin-bottom: 2rem;
  }
  
  .hero-buttons {
    flex-direction: column;
    gap: 15px;
    align-items: center;
    margin-bottom: 1.5rem;
  }
  
  .btn-lg {
    width: 100%;
    max-width: 300px;
  }
}

@media (max-width: 576px) {
  .hero-section {
    height: 60vh;
    min-height: 450px;
  }
  
  .hero-title {
    font-size: 2.5rem;
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
    padding: 12px 25px;
    font-size: 1rem;
  }
}
</style>

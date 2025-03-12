// ナビゲーションメニューの開閉
document.addEventListener('DOMContentLoaded', function() {
  const menuToggle = document.querySelector('.menu-toggle');
  const siteNav = document.querySelector('.site-nav');
  
  if (menuToggle && siteNav) {
    menuToggle.addEventListener('click', function() {
      siteNav.classList.toggle('nav-open');
      menuToggle.classList.toggle('is-active');
      document.body.classList.toggle('nav-active');
    });
    
    // 画面サイズが変わった時の処理
    window.addEventListener('resize', function() {
      if (window.innerWidth > 768 && siteNav.classList.contains('nav-open')) {
        siteNav.classList.remove('nav-open');
        menuToggle.classList.remove('is-active');
        document.body.classList.remove('nav-active');
      }
    });
    
    // ナビゲーションリンクをクリックした時の処理
    const navLinks = siteNav.querySelectorAll('.page-link');
    navLinks.forEach(link => {
      link.addEventListener('click', function() {
        if (window.innerWidth <= 768) {
          siteNav.classList.remove('nav-open');
          menuToggle.classList.remove('is-active');
          document.body.classList.remove('nav-active');
        }
      });
    });
  }
  
  // スクロール時のヘッダースタイル変更
  const siteHeader = document.querySelector('.site-header');
  let lastScrollTop = 0;
  
  window.addEventListener('scroll', function() {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 100) {
      siteHeader.classList.add('scrolled');
      
      if (scrollTop > lastScrollTop) {
        // 下にスクロール
        siteHeader.classList.add('header-hidden');
      } else {
        // 上にスクロール
        siteHeader.classList.remove('header-hidden');
      }
    } else {
      siteHeader.classList.remove('scrolled');
      siteHeader.classList.remove('header-hidden');
    }
    
    lastScrollTop = scrollTop;
  });
  
  // コードブロックのコピーボタン
  const codeBlocks = document.querySelectorAll('pre');
  codeBlocks.forEach(block => {
    const copyButton = document.createElement('button');
    copyButton.className = 'copy-button';
    copyButton.innerHTML = '<i class="fas fa-copy"></i>';
    copyButton.title = 'コードをコピー';
    
    // ボタンの配置
    block.style.position = 'relative';
    block.appendChild(copyButton);
    
    copyButton.addEventListener('click', function() {
      const code = block.querySelector('code').innerText;
      navigator.clipboard.writeText(code).then(() => {
        copyButton.innerHTML = '<i class="fas fa-check"></i>';
        copyButton.classList.add('copied');
        
        setTimeout(() => {
          copyButton.innerHTML = '<i class="fas fa-copy"></i>';
          copyButton.classList.remove('copied');
        }, 2000);
      });
    });
  });
  
  // 目次の自動生成（記事ページのみ）
  if (document.querySelector('.post-content')) {
    const headings = document.querySelectorAll('.post-content h2, .post-content h3');
    if (headings.length > 2) {
      const tocContainer = document.createElement('div');
      tocContainer.className = 'table-of-contents';
      
      const tocTitle = document.createElement('h2');
      tocTitle.textContent = '目次';
      tocContainer.appendChild(tocTitle);
      
      const tocList = document.createElement('ul');
      tocContainer.appendChild(tocList);
      
      headings.forEach((heading, index) => {
        // 見出しにIDを付与
        if (!heading.id) {
          heading.id = `heading-${index}`;
        }
        
        const listItem = document.createElement('li');
        listItem.className = heading.tagName === 'H3' ? 'toc-h3' : '';
        
        const link = document.createElement('a');
        link.href = `#${heading.id}`;
        link.textContent = heading.textContent;
        
        listItem.appendChild(link);
        tocList.appendChild(listItem);
      });
      
      // 最初の見出しの前に目次を挿入
      if (headings.length > 0) {
        const postContent = document.querySelector('.post-content');
        postContent.insertBefore(tocContainer, headings[0]);
      }
    }
  }
});

// ページのトップに戻るボタン
window.addEventListener('scroll', function() {
  const backToTopButton = document.querySelector('.back-to-top-button');
  
  if (backToTopButton) {
    if (window.pageYOffset > 300) {
      backToTopButton.classList.add('show');
    } else {
      backToTopButton.classList.remove('show');
    }
  }
});

// 遅延読み込み
document.addEventListener('DOMContentLoaded', function() {
  const lazyImages = [].slice.call(document.querySelectorAll('img.lazy'));
  
  if ('IntersectionObserver' in window) {
    let lazyImageObserver = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          let lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          if (lazyImage.dataset.srcset) {
            lazyImage.srcset = lazyImage.dataset.srcset;
          }
          lazyImage.classList.remove('lazy');
          lazyImageObserver.unobserve(lazyImage);
        }
      });
    });
    
    lazyImages.forEach(function(lazyImage) {
      lazyImageObserver.observe(lazyImage);
    });
  } else {
    // Fallback for browsers without IntersectionObserver support
    let active = false;
    
    const lazyLoad = function() {
      if (active === false) {
        active = true;
        
        setTimeout(function() {
          lazyImages.forEach(function(lazyImage) {
            if ((lazyImage.getBoundingClientRect().top <= window.innerHeight && lazyImage.getBoundingClientRect().bottom >= 0) && getComputedStyle(lazyImage).display !== 'none') {
              lazyImage.src = lazyImage.dataset.src;
              if (lazyImage.dataset.srcset) {
                lazyImage.srcset = lazyImage.dataset.srcset;
              }
              lazyImage.classList.remove('lazy');
              
              lazyImages = lazyImages.filter(function(image) {
                return image !== lazyImage;
              });
              
              if (lazyImages.length === 0) {
                document.removeEventListener('scroll', lazyLoad);
                window.removeEventListener('resize', lazyLoad);
                window.removeEventListener('orientationchange', lazyLoad);
              }
            }
          });
          
          active = false;
        }, 200);
      }
    };
    
    document.addEventListener('scroll', lazyLoad);
    window.addEventListener('resize', lazyLoad);
    window.addEventListener('orientationchange', lazyLoad);
    lazyLoad();
  }
});

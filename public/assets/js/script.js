// ─── NAVBAR SCROLL EFFECT ─────────────────────────────────────────────────────
const navbar = document.getElementById('main-navbar');

window.addEventListener('scroll', () => {
  if (!navbar) return;
  if (window.scrollY > 20) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
}, { passive: true });

// ─── MOBILE HAMBURGER MENU ────────────────────────────────────────────────────
const hamburgerBtn  = document.getElementById('hamburger-btn');
const mobileDrawer  = document.getElementById('mobile-drawer');
const mobileOverlay = document.getElementById('mobile-overlay');
const mobileClose   = document.getElementById('mobile-close-btn');

function openDrawer() {
  if(hamburgerBtn) {
    hamburgerBtn.classList.add('open');
    hamburgerBtn.setAttribute('aria-expanded', 'true');
  }
  if(mobileDrawer) {
    mobileDrawer.classList.add('open');
    mobileDrawer.setAttribute('aria-hidden', 'false');
  }
  if(mobileOverlay) mobileOverlay.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeDrawer() {
  if(hamburgerBtn) {
    hamburgerBtn.classList.remove('open');
    hamburgerBtn.setAttribute('aria-expanded', 'false');
  }
  if(mobileDrawer) {
    mobileDrawer.classList.remove('open');
    mobileDrawer.setAttribute('aria-hidden', 'true');
  }
  if(mobileOverlay) mobileOverlay.classList.remove('active');
  document.body.style.overflow = '';
}

if (hamburgerBtn) {
  hamburgerBtn.addEventListener('click', () => {
    (mobileDrawer && mobileDrawer.classList.contains('open')) ? closeDrawer() : openDrawer();
  });
}

if (mobileClose) mobileClose.addEventListener('click', closeDrawer);
if (mobileOverlay) mobileOverlay.addEventListener('click', closeDrawer);

// Close drawer when any mobile nav link is tapped
document.querySelectorAll('.mobile-nav-link').forEach(link => {
  link.addEventListener('click', closeDrawer);
});

// Close on ESC key
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeDrawer();
});


// ─── SCROLL REVEAL ANIMATION ──────────────────────────────────────────────────
const revealElements = document.querySelectorAll(
  '.category-card, .feature-item, .product-card, .new-season__content, .new-season__model, .best-of__header'
);

revealElements.forEach(el => el.classList.add('reveal'));

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        // Stagger delay for grid children
        const delay = entry.target.dataset.delay || 0;
        setTimeout(() => {
          entry.target.classList.add('visible');
        }, Number(delay));
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12, rootMargin: '0px 0px -40px 0px' }
);

// Add stagger delays to grid items
document.querySelectorAll('.category-card').forEach((el, i) => el.dataset.delay = i * 100);
document.querySelectorAll('.feature-item').forEach((el, i) => el.dataset.delay = i * 80);
document.querySelectorAll('.product-card').forEach((el, i) => el.dataset.delay = i * 100);

revealElements.forEach(el => observer.observe(el));

// ─── WISHLIST TOGGLE ──────────────────────────────────────────────────────────
document.querySelectorAll('.wishlist-icon').forEach(btn => {
  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    btn.classList.toggle('active');
    const svg = btn.querySelector('svg');
    if (btn.classList.contains('active')) {
      svg.setAttribute('fill', '#c0392b');
      svg.setAttribute('stroke', '#c0392b');
    } else {
      svg.setAttribute('fill', 'none');
      svg.setAttribute('stroke', 'currentColor');
    }
  });
});


// ─── NEWSLETTER FORM ──────────────────────────────────────────────────────────
const newsletterForm = document.getElementById('newsletter-form');
if (newsletterForm) {
  newsletterForm.addEventListener('submit', (e) => {
    const input = document.getElementById('newsletter-email');
    const btn = document.getElementById('newsletter-submit');
    
    if (input.value && input.value.includes('@')) {
      btn.textContent = 'SUBSCRIBED ✓';
      btn.style.background = '#2a6644';
      input.value = '';
      setTimeout(() => {
        btn.textContent = 'SUBSCRIBE';
        btn.style.background = '';
      }, 3000);
    } else {
      input.style.borderColor = 'rgba(200,80,80,0.6)';
      setTimeout(() => input.style.borderColor = '', 2000);
    }
  });
}

// ─── SEARCH OVERLAY ───────────────────────────────────────────────────────────
const searchBtn = document.getElementById('search-btn');
if (searchBtn) {
  searchBtn.addEventListener('click', () => {
    const overlay = document.createElement('div');
    overlay.id = 'search-overlay';
    overlay.style.cssText = `
      position: fixed;
      inset: 0;
      background: rgba(255,255,255,0.97);
      z-index: 9999;
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.3s ease;
    `;
    
    overlay.innerHTML = `
      <div style="text-align: center; width: 100%; max-width: 560px; padding: 0 24px;">
        <div style="font-family: 'Cormorant Garamond', serif; font-size: 14px; letter-spacing: 0.2em; color: #a8832a; margin-bottom: 24px;">SEARCH</div>
        <div style="display: flex; border-bottom: 1.5px solid #2a2a2a; align-items: center; gap: 10px;">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6b6b6b" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input id="search-input" type="text" placeholder="Search for products..." 
            style="flex:1; border:none; outline:none; font-family:'Inter',sans-serif; font-size:18px; padding:12px 0; background:transparent; color:#2a2a2a;" 
            autofocus />
        </div>
        <p style="font-size:11px; color:#aaa; margin-top:14px; letter-spacing:0.08em;">Press ESC to close</p>
      </div>
    `;
    
    document.body.appendChild(overlay);
    requestAnimationFrame(() => { overlay.style.opacity = '1'; });
    
    const close = () => {
      overlay.style.opacity = '0';
      setTimeout(() => overlay.remove(), 300);
    };
    
    overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); }, { once: true });
  });
}

// ─── FULLY SYNCHRONIZED REAL CART LOGIC ──────────────────────────────────────

let arteviaCart = [];
try {
  arteviaCart = JSON.parse(localStorage.getItem('artevia_cart_data')) || [];
} catch (e) {
  console.error('Error parsing cart data', e);
  arteviaCart = [];
}

function saveCart() {
  localStorage.setItem('artevia_cart_data', JSON.stringify(arteviaCart));
  syncCartDrawer();
}

function updateCartUI() {
  const count = document.getElementById('cart-count');
  const wCount = document.getElementById('w-cart-count');
  
  const totalQty = arteviaCart.reduce((sum, item) => sum + item.qty, 0);
  if(count) count.textContent = totalQty;
  if(wCount) wCount.textContent = totalQty;
}

// ─── DYNAMIC PRODUCT FETCHING ────────────────────────────────────────────────
async function loadDynamicProducts() {
  const grid = document.getElementById('dynamic-products-grid');
  if (!grid) return;

  const category = grid.getAttribute('data-category');
  const collection = grid.getAttribute('data-collection');
  
  let url = '/api/products?';
  if (category) url += `category=${category}&`;
  if (collection) url += `collectionName=${collection}`;

  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error('Network response was not ok');
    const products = await res.json();

    grid.innerHTML = '';
    products.forEach(p => {
      const card = document.createElement('a');
      card.href = '#';
      card.className = 'cp-card';
      card.innerHTML = `
        <div class="cp-card-img-wrapper">
          <img src="${p.imageUrl}" alt="${p.name}" class="cp-card-img" />
          <div class="cp-card-actions">
            <button class="cp-action-btn cp-fav-btn" onclick="event.preventDefault(); toggleFavorite(this);" aria-label="Add to Favorites">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
            </button>
            <button class="cp-action-btn cp-add-btn" onclick="event.preventDefault(); showCartModal(this);" aria-label="Add to Cart">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M9 20a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm7 0a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-9.8-3.4h11.6l2.3-10.4H5.4l-.8-3.7H1v2h2.2l3.4 15.6.8-3.5z"></path></svg>
              SEPETE EKLE
            </button>
          </div>
        </div>
        <div class="cp-card-info">
          <div class="cp-card-title">${p.name}</div>
          <div class="cp-card-price">₺${p.price}</div>
          <div class="cp-card-arrow">&rarr;</div>
        </div>
      `;
      grid.appendChild(card);
    });
  } catch (err) {
    console.error('Error fetching products:', err);
    grid.innerHTML = '<p style="text-align:center; width:100%;">Failed to load products. Please try again later.</p>';
  }
}

document.addEventListener('DOMContentLoaded', loadDynamicProducts);

function syncCartDrawer() {
  const container = document.querySelector('.cart-drawer-items');
  const countSpan = document.getElementById('w-cart-count');
  const totalSpan = document.getElementById('mock-total-price');
  
  if (!container) return;

  // Clear drawer items
  container.innerHTML = '';
  
  let totalQty = 0;
  let totalPrice = 0;

  if (arteviaCart.length === 0) {
    container.innerHTML = '<div style="color:rgba(255,255,255,0.5); text-align:center; margin-top:50px; font-family:\'Outfit\', sans-serif; letter-spacing:0.1em;">SEPETİNİZ BOŞ.</div>';
  } else {
    arteviaCart.forEach((item, index) => {
      totalQty += item.qty;
      totalPrice += item.price * item.qty;
      
      const itemHTML = `
        <div class="cart-drawer-item">
          <img src="${item.image}" alt="${item.title}" class="cart-item-img" />
          <div class="cart-item-details">
            <div class="cart-item-title">${item.title}</div>
            <div class="cart-item-variant">Beden: L | Renk: Standart</div>
            <div class="cart-item-price">₺${item.price}</div>
            <div style="display:flex; align-items:center; gap:15px;">
              <div class="cart-item-qty">
                <button class="qty-btn" onclick="updateCartItem(${index}, -1)">-</button>
                <span>${item.qty}</span>
                <button class="qty-btn" onclick="updateCartItem(${index}, 1)">+</button>
              </div>
              <button onclick="removeCartItem(${index})" style="background:none; border:none; color:rgba(255,255,255,0.5); font-family:'Outfit', sans-serif; font-size:11px; text-decoration:underline; cursor:pointer;">Sil</button>
            </div>
          </div>
        </div>
      `;
      container.innerHTML += itemHTML;
    });
  }

  // Update navbar counter
  if (countSpan) countSpan.innerText = totalQty;
  // Update total price
  if (totalSpan) totalSpan.innerText = totalPrice;
}

// Initial sync on page load
document.addEventListener("DOMContentLoaded", () => {
  syncCartDrawer();
});

function showCartModal(btn) {
  // DOM Traversal to extract product info
  if (btn) {
    const card = btn.closest('a.cp-card');
    if (card) {
      const titleEl = card.querySelector('.cp-card-title');
      const priceEl = card.querySelector('.cp-card-price');
      const imgEl = card.querySelector('.cp-card-img');
      
      if (titleEl && priceEl && imgEl) {
        const title = titleEl.innerText.trim();
        // Extract numbers from price string like "₺2500" or "2.500"
        const priceStr = priceEl.innerText.replace(/[^0-9]/g, '');
        const price = parseInt(priceStr) || 0;
        const image = imgEl.getAttribute('src');
        
        // Check if item already in cart
        const existingItem = arteviaCart.find(i => i.title === title);
        if (existingItem) {
          existingItem.qty += 1;
        } else {
          arteviaCart.push({ title, price, image, qty: 1 });
        }
        
        saveCart();
      }
    }
  }

  // Show modal
  const modal = document.getElementById('cartModal');
  if (modal) modal.classList.add('active');
}

function closeCartModal() {
  const modal = document.getElementById('cartModal');
  if (modal) modal.classList.remove('active');
}

function openCartDrawer() {
  const overlay = document.getElementById('cartDrawerOverlay');
  const drawer = document.getElementById('cartDrawer');
  if(overlay && drawer) {
    overlay.classList.add('active');
    drawer.classList.add('active');
  }
}

function closeCartDrawer() {
  const overlay = document.getElementById('cartDrawerOverlay');
  const drawer = document.getElementById('cartDrawer');
  if(overlay && drawer) {
    overlay.classList.remove('active');
    drawer.classList.remove('active');
  }
}

function updateCartItem(index, change) {
  if (arteviaCart[index]) {
    arteviaCart[index].qty += change;
    if (arteviaCart[index].qty < 1) {
      removeCartItem(index);
    } else {
      saveCart();
    }
  }
}

function removeCartItem(index) {
  arteviaCart.splice(index, 1);
  saveCart();
}

// ─── FAVORITES LOGIC ───────────────────────────────────────────────────────────
let arteviaFavs = [];
try {
  arteviaFavs = JSON.parse(localStorage.getItem('artevia_fav_data')) || [];
} catch (e) {
  console.error('Error parsing fav data', e);
  arteviaFavs = [];
}

function saveFavs() {
  localStorage.setItem('artevia_fav_data', JSON.stringify(arteviaFavs));
  syncFavDrawer();
}

function syncFavDrawer() {
  const container = document.querySelector('.fav-drawer-items');
  if (!container) return;

  container.innerHTML = '';
  
  if (arteviaFavs.length === 0) {
    container.innerHTML = '<div style="color:rgba(255,255,255,0.5); text-align:center; margin-top:50px; font-family:\'Outfit\', sans-serif; letter-spacing:0.1em;">FAVORİ LİSTENİZ BOŞ.</div>';
  } else {
    arteviaFavs.forEach((item, index) => {
      const itemHTML = `
        <div class="cart-drawer-item">
          <img src="${item.image}" alt="${item.title}" class="cart-item-img" />
          <div class="cart-item-details">
            <div class="cart-item-title">${item.title}</div>
            <div class="cart-item-price">₺${item.price}</div>
            <div style="display:flex; align-items:center; gap:15px; margin-top:auto;">
              <button onclick="removeFavItem(${index})" style="background:none; border:none; color:rgba(255,255,255,0.5); font-family:'Outfit', sans-serif; font-size:11px; text-decoration:underline; cursor:pointer;">Kaldır</button>
            </div>
          </div>
        </div>
      `;
      container.innerHTML += itemHTML;
    });
  }
  
  // Sync heart icons on current page
  document.querySelectorAll('a.cp-card').forEach(card => {
     const titleEl = card.querySelector('.cp-card-title');
     const favBtn = card.querySelector('.cp-fav-btn');
     if(titleEl && favBtn) {
       const title = titleEl.innerText.trim();
       const isFav = arteviaFavs.find(i => i.title === title);
       if(isFav) favBtn.classList.add('active-fav');
       else favBtn.classList.remove('active-fav');
     }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  syncFavDrawer();
});

function toggleFavorite(btn) {
  if (btn) {
    const card = btn.closest('a.cp-card');
    if (card) {
      const titleEl = card.querySelector('.cp-card-title');
      const priceEl = card.querySelector('.cp-card-price');
      const imgEl = card.querySelector('.cp-card-img');
      
      if (titleEl && priceEl && imgEl) {
        const title = titleEl.innerText.trim();
        const priceStr = priceEl.innerText.replace(/[^0-9]/g, '');
        const price = parseInt(priceStr) || 0;
        const image = imgEl.getAttribute('src');
        
        const existingIndex = arteviaFavs.findIndex(i => i.title === title);
        if (existingIndex > -1) {
          arteviaFavs.splice(existingIndex, 1);
          btn.classList.remove('active-fav');
        } else {
          arteviaFavs.push({ title, price, image });
          btn.classList.add('active-fav');
        }
        
        saveFavs();
      }
    }
  }
}

function removeFavItem(index) {
  arteviaFavs.splice(index, 1);
  saveFavs();
}

function openFavDrawer() {
  const overlay = document.getElementById('favDrawerOverlay');
  const drawer = document.getElementById('favDrawer');
  if(overlay && drawer) {
    overlay.classList.add('active');
    drawer.classList.add('active');
  }
}

function closeFavDrawer() {
  const overlay = document.getElementById('favDrawerOverlay');
  const drawer = document.getElementById('favDrawer');
  if(overlay && drawer) {
    overlay.classList.remove('active');
    drawer.classList.remove('active');
  }
}

// ─── MOCK AUTHENTICATION LOGIC ───────────────────────────────────────────────
let isUserLoggedIn = localStorage.getItem('artevia_auth_state') !== null 
  ? JSON.parse(localStorage.getItem('artevia_auth_state')) 
  : true; // Default to true if not set

function toggleAuthState(status) {
  isUserLoggedIn = status;
  localStorage.setItem('artevia_auth_state', JSON.stringify(status));
  
  const authButtonsList = document.querySelectorAll('#auth-buttons');
  const userProfileMenus = document.querySelectorAll('#user-profile-menu');
  
  authButtonsList.forEach(el => {
    el.style.display = isUserLoggedIn ? 'none' : 'flex';
  });
  
  userProfileMenus.forEach(el => {
    el.style.display = isUserLoggedIn ? 'inline-block' : 'none';
  });
  
  // Hide Favorites and Cart buttons when logged out
  const navLinks = document.querySelectorAll('.w-nav-links li');
  navLinks.forEach(li => {
    const text = li.textContent.toUpperCase();
    if (text.includes('FAVORİLER') || text.includes('SEPET')) {
      li.style.display = isUserLoggedIn ? '' : 'none';
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  toggleAuthState(isUserLoggedIn);
});

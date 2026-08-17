import React, { useState, useEffect } from 'react';
import { Eye, EyeOff, Mail, Lock, User } from 'lucide-react';
import { useLocation } from 'react-router-dom';

const AuthPage = () => {
  const location = useLocation();
  const queryParams = new URLSearchParams(location.search);
  const initialMode = queryParams.get('mode') !== 'signup';
  
  const [isLogin, setIsLogin] = useState(initialMode);
  const [showPassword, setShowPassword] = useState(false);
  
  // Form State
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  const handleInputChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
    setErrorMsg('');
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    setErrorMsg('');

    // Simulate API Call
    setTimeout(() => {
      setLoading(false);
      if (!isLogin) {
        // Sign Up Success
        if (!formData.name || !formData.email || !formData.password) {
          setErrorMsg('Please fill in all fields.');
          return;
        }
        setSuccessMsg('Account created successfully. Please log in.');
        setIsLogin(true);
        setFormData({ name: '', email: formData.email, password: '' });
      } else {
        // Log In Success
        if (!formData.email || !formData.password) {
          setErrorMsg('Please enter both email and password.');
          return;
        }
        // Redirect to main home page (outside React SPA)
        window.location.href = '/';
      }
    }, 1000);
  };

  return (
    <div style={{ backgroundColor: '#1a3a2a', minHeight: '100vh', display: 'flex', flexDirection: 'column', fontFamily: "'Outfit', sans-serif" }}>
      
      {/* Top Navbar mimic for seamless integration */}
      <nav style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '30px 60px', borderBottom: '1px solid rgba(198,168,124,0.2)' }}>
        <a href="/" style={{ fontFamily: "'Cormorant Garamond', serif", fontSize: '32px', color: '#c6a87c', textDecoration: 'none', fontStyle: 'italic' }}>Artévia</a>
      </nav>

      {/* Main Content Area */}
      <div style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '2rem' }}>
        <div style={{ width: '100%', maxWidth: '400px', backgroundColor: 'transparent' }}>
          
          <h1 style={{ fontFamily: "'Cormorant Garamond', serif", fontSize: '36px', color: '#c6a87c', textAlign: 'center', marginBottom: '10px', fontStyle: 'italic' }}>
            {isLogin ? 'Welcome Back' : 'Join Artévia'}
          </h1>
          
          <p style={{ color: '#c6a87c', textAlign: 'center', fontSize: '14px', letterSpacing: '0.1em', marginBottom: '30px', opacity: 0.8 }}>
            {isLogin ? 'Enter your details to access your account.' : 'Create an account for exclusive access.'}
          </p>

          {successMsg && (
            <div style={{ padding: '12px', border: '1px solid #c6a87c', backgroundColor: 'rgba(198,168,124,0.1)', color: '#c6a87c', marginBottom: '20px', textAlign: 'center', fontSize: '13px', letterSpacing: '0.05em' }}>
              {successMsg}
            </div>
          )}

          {errorMsg && (
            <div style={{ padding: '12px', border: '1px solid #ff4d4d', backgroundColor: 'rgba(255,77,77,0.1)', color: '#ff4d4d', marginBottom: '20px', textAlign: 'center', fontSize: '13px', letterSpacing: '0.05em' }}>
              {errorMsg}
            </div>
          )}

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
            
            {!isLogin && (
              <div style={{ position: 'relative' }}>
                <User size={18} style={{ position: 'absolute', left: '15px', top: '50%', transform: 'translateY(-50%)', color: '#c6a87c', opacity: 0.6 }} />
                <input 
                  type="text" 
                  name="name"
                  placeholder="Full Name"
                  value={formData.name}
                  onChange={handleInputChange}
                  style={{ width: '100%', padding: '15px 15px 15px 45px', backgroundColor: 'transparent', border: '1px solid rgba(198,168,124,0.4)', color: '#fff', fontSize: '14px', letterSpacing: '0.1em', outline: 'none' }}
                  onFocus={(e) => e.target.style.borderColor = '#c6a87c'}
                  onBlur={(e) => e.target.style.borderColor = 'rgba(198,168,124,0.4)'}
                />
              </div>
            )}

            <div style={{ position: 'relative' }}>
              <Mail size={18} style={{ position: 'absolute', left: '15px', top: '50%', transform: 'translateY(-50%)', color: '#c6a87c', opacity: 0.6 }} />
              <input 
                type="email" 
                name="email"
                placeholder="Email Address"
                value={formData.email}
                onChange={handleInputChange}
                style={{ width: '100%', padding: '15px 15px 15px 45px', backgroundColor: 'transparent', border: '1px solid rgba(198,168,124,0.4)', color: '#fff', fontSize: '14px', letterSpacing: '0.1em', outline: 'none' }}
                onFocus={(e) => e.target.style.borderColor = '#c6a87c'}
                onBlur={(e) => e.target.style.borderColor = 'rgba(198,168,124,0.4)'}
              />
            </div>

            <div style={{ position: 'relative' }}>
              <Lock size={18} style={{ position: 'absolute', left: '15px', top: '50%', transform: 'translateY(-50%)', color: '#c6a87c', opacity: 0.6 }} />
              <input 
                type={showPassword ? 'text' : 'password'} 
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleInputChange}
                style={{ width: '100%', padding: '15px 45px 15px 45px', backgroundColor: 'transparent', border: '1px solid rgba(198,168,124,0.4)', color: '#fff', fontSize: '14px', letterSpacing: '0.1em', outline: 'none' }}
                onFocus={(e) => e.target.style.borderColor = '#c6a87c'}
                onBlur={(e) => e.target.style.borderColor = 'rgba(198,168,124,0.4)'}
              />
              <button 
                type="button" 
                onClick={() => setShowPassword(!showPassword)}
                style={{ position: 'absolute', right: '15px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', color: '#c6a87c', cursor: 'pointer', opacity: 0.6 }}
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>

            <button 
              type="submit" 
              disabled={loading}
              style={{ width: '100%', padding: '15px', backgroundColor: '#c6a87c', color: '#1a3a2a', border: 'none', fontWeight: 600, letterSpacing: '0.15em', textTransform: 'uppercase', fontSize: '13px', cursor: 'pointer', marginTop: '10px', transition: 'background-color 0.3s' }}
              onMouseOver={(e) => e.target.style.backgroundColor = '#d8bd94'}
              onMouseOut={(e) => e.target.style.backgroundColor = '#c6a87c'}
            >
              {loading ? 'Processing...' : (isLogin ? 'Log In' : 'Sign Up')}
            </button>
          </form>

          <div style={{ marginTop: '30px', textAlign: 'center' }}>
            <p style={{ color: '#c6a87c', fontSize: '13px', letterSpacing: '0.1em', opacity: 0.8 }}>
              {isLogin ? "Don't have an account? " : "Already have an account? "}
              <button 
                onClick={() => { setIsLogin(!isLogin); setSuccessMsg(''); setErrorMsg(''); }}
                style={{ background: 'none', border: 'none', color: '#fff', cursor: 'pointer', fontWeight: 500, letterSpacing: '0.1em', padding: 0, textDecoration: 'underline' }}
              >
                {isLogin ? 'Sign up' : 'Log in'}
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AuthPage;

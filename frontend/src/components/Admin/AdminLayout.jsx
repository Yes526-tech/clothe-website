import React, { useState } from 'react';
import { LayoutDashboard, ShoppingBag, Package, Users, Settings, Bell, Search, Menu, Crown } from 'lucide-react';
import { Link, useLocation } from 'react-router-dom';

const AdminLayout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const location = useLocation();

  const navItems = [
    { name: 'Dashboard', path: '/admin', icon: <LayoutDashboard size={20} /> },
    { name: 'Inventory', path: '/admin/inventory', icon: <Package size={20} /> },
    { name: 'Customers', path: '/admin/customers', icon: <Users size={20} /> },
  ];

  return (
    <div className="min-h-screen bg-parchment-200 flex flex-col md:flex-row font-sans">
      
      {/* Sidebar */}
      <aside className={`${sidebarOpen ? 'w-64' : 'w-20'} transition-all duration-300 bg-burgundy-900 text-parchment-100 border-r border-gold-500/20 hidden md:flex flex-col shadow-xl z-20`}>
        <div className="h-16 flex items-center justify-center border-b border-gold-500/20 px-4">
          <Crown className={`text-gold-500 transition-all ${sidebarOpen ? 'w-8 h-8 mr-2' : 'w-10 h-10'}`} />
          {sidebarOpen && <span className="font-serif text-2xl tracking-widest text-gold-400">Artévia</span>}
        </div>
        
        <nav className="flex-1 py-8 px-4 space-y-2">
          {navItems.map((item, idx) => (
            <Link key={idx} to={item.path} className={`flex items-center px-3 py-3 rounded-lg hover:bg-burgundy-700 hover:text-gold-400 transition-colors group ${location.pathname === item.path ? 'bg-burgundy-700 text-gold-400' : ''}`}>
              <span className={`${sidebarOpen ? 'mr-3' : 'mx-auto'} ${location.pathname === item.path ? 'text-gold-400' : 'text-gold-500/70'} group-hover:text-gold-400`}>
                {item.icon}
              </span>
              {sidebarOpen && <span className="font-serif tracking-wide">{item.name}</span>}
            </Link>
          ))}
        </nav>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        
        {/* Top Navbar */}
        <header className="h-16 bg-parchment-100 border-b border-burgundy-900/10 flex items-center justify-between px-4 sm:px-6 lg:px-8 shadow-sm z-10">
          <div className="flex items-center">
            <button onClick={() => setSidebarOpen(!sidebarOpen)} className="text-burgundy-900 hover:text-gold-600 focus:outline-none hidden md:block">
              <Menu size={24} />
            </button>
            <div className="ml-4 flex-1 max-w-lg hidden sm:flex items-center">
              <div className="relative w-full">
                <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                  <Search className="h-5 w-5 text-burgundy-900/40" />
                </div>
                <input
                  type="text"
                  placeholder="Search the archives..."
                  className="block w-full pl-10 pr-3 py-2 border border-burgundy-900/20 rounded-md leading-5 bg-parchment-200 text-burgundy-900 placeholder-burgundy-900/40 focus:outline-none focus:bg-white focus:ring-1 focus:ring-gold-500 focus:border-gold-500 font-serif italic sm:text-sm transition-colors"
                />
              </div>
            </div>
          </div>
          
          <div className="flex items-center space-x-4">
            <button className="relative text-burgundy-900 hover:text-gold-600 transition-colors">
              <Bell size={24} />
              <span className="absolute top-0 right-0 block h-2.5 w-2.5 rounded-full bg-emerald-700 ring-2 ring-parchment-100"></span>
            </button>
            <div className="flex items-center space-x-3 border-l border-burgundy-900/20 pl-4">
              <img className="h-9 w-9 rounded-full border border-gold-500 shadow-sm" src="https://i.pravatar.cc/150?u=admin" alt="Admin profile" />
              <div className="hidden sm:block text-sm">
                <p className="text-burgundy-900 font-serif font-bold">Lord Administrator</p>
                <p className="text-burgundy-900/60 font-serif italic text-xs">Master of Coin</p>
              </div>
            </div>
          </div>
        </header>

        {/* Dynamic Content goes here */}
        <main className="flex-1 overflow-y-auto bg-parchment-100/50 p-6 lg:p-8">
          {children}
        </main>
      </div>
    </div>
  );
};
export default AdminLayout;

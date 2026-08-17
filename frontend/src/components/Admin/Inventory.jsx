import React, { useState, useEffect } from 'react';
import { Edit2, Trash2, Plus, Save, X } from 'lucide-react';

const Inventory = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isEditing, setIsEditing] = useState(false);
  const [currentItem, setCurrentItem] = useState({ name: '', category: '', stock: 0, price: 0, imageUrl: '' });

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = () => {
    setLoading(true);
    fetch('/api/products')
      .then(res => res.json())
      .then(data => {
        setItems(data);
        setLoading(false);
      });
  };

  const handleSave = () => {
    const method = currentItem.id ? 'PUT' : 'POST';
    const url = currentItem.id ? `/api/products/${currentItem.id}` : '/api/products';
    
    fetch(url, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(currentItem)
    }).then(() => {
      setIsEditing(false);
      fetchItems();
    });
  };

  const handleDelete = (id) => {
    if(confirm("Are you sure you wish to discard this item from the archives?")) {
      fetch(`/api/products/${id}`, { method: 'DELETE' }).then(() => fetchItems());
    }
  };

  const openEditor = (item = { name: '', category: 'men', stock: 0, price: 0, imageUrl: '/assets/images/placeholder.jpg' }) => {
    setCurrentItem(item);
    setIsEditing(true);
  };

  return (
    <div>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-serif text-burgundy-900">Armory & Attire</h1>
        <button onClick={() => openEditor()} className="flex items-center px-4 py-2 bg-burgundy-900 text-gold-400 font-serif text-sm rounded shadow-sm hover:bg-burgundy-700 transition-colors">
          <Plus size={16} className="mr-2" /> Forge New Item
        </button>
      </div>

      {isEditing && (
        <div className="bg-white p-6 rounded-xl shadow-sm border border-gold-500/30 mb-8">
          <h2 className="text-xl font-serif text-burgundy-900 mb-4">{currentItem.id ? 'Edit Item' : 'New Item'}</h2>
          <div className="grid grid-cols-2 gap-4 mb-4">
            <input className="border border-burgundy-900/20 p-2 rounded focus:outline-none focus:border-gold-500 font-serif" placeholder="Item Name" value={currentItem.name} onChange={e => setCurrentItem({...currentItem, name: e.target.value})} />
            <input className="border border-burgundy-900/20 p-2 rounded focus:outline-none focus:border-gold-500 font-serif" placeholder="Category" value={currentItem.category} onChange={e => setCurrentItem({...currentItem, category: e.target.value})} />
            <input className="border border-burgundy-900/20 p-2 rounded focus:outline-none focus:border-gold-500 font-serif" type="number" placeholder="Price (Gold)" value={currentItem.price} onChange={e => setCurrentItem({...currentItem, price: parseFloat(e.target.value)})} />
            <input className="border border-burgundy-900/20 p-2 rounded focus:outline-none focus:border-gold-500 font-serif" type="number" placeholder="Stock" value={currentItem.stock} onChange={e => setCurrentItem({...currentItem, stock: parseInt(e.target.value, 10)})} />
            <input className="border border-burgundy-900/20 p-2 rounded focus:outline-none focus:border-gold-500 font-serif col-span-2" placeholder="Image URL" value={currentItem.imageUrl} onChange={e => setCurrentItem({...currentItem, imageUrl: e.target.value})} />
          </div>
          <div className="flex space-x-4">
            <button onClick={handleSave} className="flex items-center bg-emerald-700 text-white px-4 py-2 rounded shadow"><Save size={16} className="mr-2"/> Save Decrees</button>
            <button onClick={() => setIsEditing(false)} className="flex items-center bg-gray-200 text-burgundy-900 px-4 py-2 rounded shadow"><X size={16} className="mr-2"/> Cancel</button>
          </div>
        </div>
      )}

      {loading ? (
        <div className="text-center py-10 font-serif italic text-burgundy-900">Consulting the archives...</div>
      ) : (
        <div className="bg-white rounded-xl shadow-sm border border-burgundy-900/10 overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left border-collapse">
              <thead>
                <tr className="bg-burgundy-900/5 border-b border-burgundy-900/10">
                  <th className="px-6 py-4 font-serif text-sm text-burgundy-900">Item</th>
                  <th className="px-6 py-4 font-serif text-sm text-burgundy-900">Category</th>
                  <th className="px-6 py-4 font-serif text-sm text-burgundy-900">Stock Status</th>
                  <th className="px-6 py-4 font-serif text-sm text-burgundy-900">Value</th>
                  <th className="px-6 py-4 font-serif text-sm text-burgundy-900 text-right">Decrees</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-burgundy-900/10">
                {items.map((item) => (
                  <tr key={item.id} className="hover:bg-parchment-200/30 transition-colors">
                    <td className="px-6 py-4 flex items-center">
                      <div className="h-10 w-10 bg-parchment-300 rounded border border-gold-500/30 mr-4 overflow-hidden">
                        <img src={item.imageUrl} alt={item.name} className="w-full h-full object-cover" />
                      </div>
                      <span className="font-serif font-medium text-burgundy-900">{item.name}</span>
                    </td>
                    <td className="px-6 py-4 text-sm text-gray-600 font-sans">{item.category}</td>
                    <td className="px-6 py-4">
                      <span className={`px-3 py-1 rounded-full text-xs font-medium font-sans border ${
                        item.stock > 10 ? 'bg-emerald-50 text-emerald-700 border-emerald-200' : 'bg-red-50 text-red-700 border-red-200'
                      }`}>
                        {item.stock} in Keep
                      </span>
                    </td>
                    <td className="px-6 py-4 font-serif text-burgundy-900">{item.price} G</td>
                    <td className="px-6 py-4 text-right space-x-3">
                      <button onClick={() => openEditor(item)} className="text-gold-600 hover:text-gold-500 transition-colors"><Edit2 size={18} /></button>
                      <button onClick={() => handleDelete(item.id)} className="text-burgundy-900/40 hover:text-red-700 transition-colors"><Trash2 size={18} /></button>
                    </td>
                  </tr>
                ))}
                {items.length === 0 && (
                  <tr>
                    <td colSpan="5" className="px-6 py-8 text-center text-gray-500 font-serif italic">The armory is empty.</td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};
export default Inventory;

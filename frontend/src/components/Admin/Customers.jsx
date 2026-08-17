import React from 'react';
import { Search, ChevronLeft, ChevronRight } from 'lucide-react';

const Customers = () => {
  const customers = [
    { id: 1, name: 'Lady Eleanor Vance', orders: 14, status: 'Noble (VIP)' },
    { id: 2, name: 'Sir Thomas Blackwood', orders: 3, status: 'Active' },
    { id: 3, name: 'Merchant Guild of Oakhaven', orders: 42, status: 'Wholesale' },
  ];

  return (
    <div>
      <h1 className="text-3xl font-serif text-burgundy-900 mb-6">Patrons & Nobles</h1>
      
      <div className="bg-white rounded-xl shadow-sm border border-burgundy-900/10 p-6 mb-6 flex justify-between items-center">
        <div className="relative w-72">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-burgundy-900/40" />
          <input
            type="text"
            placeholder="Search by name or crest..."
            className="w-full pl-10 pr-4 py-2 border-b-2 border-burgundy-900/20 bg-transparent focus:outline-none focus:border-gold-500 font-serif italic text-burgundy-900 transition-colors"
          />
        </div>
        <div className="text-sm font-serif text-burgundy-900/60 italic">Showing 1 to 10 of 1,248</div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-burgundy-900/10 overflow-hidden">
        <table className="w-full text-left">
          <thead>
            <tr className="bg-burgundy-900 text-parchment-100">
              <th className="px-6 py-4 font-serif font-normal">Patron Name</th>
              <th className="px-6 py-4 font-serif font-normal text-center">Treasury (Orders)</th>
              <th className="px-6 py-4 font-serif font-normal">Standing</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-burgundy-900/10">
            {customers.map((c) => (
              <tr key={c.id} className="hover:bg-parchment-100/50">
                <td className="px-6 py-4 font-serif text-burgundy-900 font-medium">{c.name}</td>
                <td className="px-6 py-4 font-sans text-center text-gray-600">{c.orders}</td>
                <td className="px-6 py-4">
                  <span className="text-sm font-serif italic text-gold-600">{c.status}</span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        
        {/* Pagination */}
        <div className="px-6 py-4 border-t border-burgundy-900/10 flex items-center justify-between bg-parchment-100/30">
          <button className="flex items-center text-sm font-serif text-burgundy-900 hover:text-gold-600">
            <ChevronLeft size={16} className="mr-1" /> Previous Scroll
          </button>
          <div className="flex space-x-2">
            {[1, 2, 3].map(page => (
              <button key={page} className={`h-8 w-8 rounded flex items-center justify-center font-serif ${page === 1 ? 'bg-burgundy-900 text-gold-400' : 'text-burgundy-900 hover:bg-parchment-200'}`}>
                {page}
              </button>
            ))}
          </div>
          <button className="flex items-center text-sm font-serif text-burgundy-900 hover:text-gold-600">
            Next Scroll <ChevronRight size={16} className="ml-1" />
          </button>
        </div>
      </div>
    </div>
  );
};
export default Customers;

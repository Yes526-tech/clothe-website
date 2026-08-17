// home.js - Specific scripts for the Collections homepage

document.addEventListener('DOMContentLoaded', () => {
  const collectionSections = document.querySelectorAll('.collection-section');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        // Unobserve if we only want it to fade in once
        // observer.unobserve(entry.target); 
      } else {
        // Optional: remove class to replay animation on scroll up/down
        entry.target.classList.remove('is-visible');
      }
    });
  }, {
    threshold: 0.3 // Trigger when 30% of the section is visible
  });

  collectionSections.forEach(section => {
    observer.observe(section);
  });
});

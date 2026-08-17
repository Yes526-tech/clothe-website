document.addEventListener('DOMContentLoaded', () => {
    const video = document.getElementById('scrollVideo');
    const section = document.querySelector('.scroll-video-section');
    
    if (!video || !section) return;

    let targetTime = 0;
    let currentTime = 0;
    
    // We use a continuous animation loop to smoothly interpolate (lerp)
    // the video's current time to the target time determined by scroll position.
    const updateVideoTime = () => {
        if (!video.duration) {
            requestAnimationFrame(updateVideoTime);
            return;
        }

        const rect = section.getBoundingClientRect();
        
        // Calculate progress based on the section's top position relative to the viewport.
        // progress is 0 when the section's top aligns with the viewport top (sticky begins).
        // progress is 1 when the section's bottom aligns with the viewport bottom (sticky ends).
        let progress = -rect.top / (rect.height - window.innerHeight);
        
        // Clamp progress between 0 and 1
        progress = Math.max(0, Math.min(1, progress));
        
        // Target time is a percentage of the total video duration
        targetTime = progress * video.duration;
        
        // Lerp (Linear Interpolation) for that buttery smooth Apple-style scrubbing
        currentTime += (targetTime - currentTime) * 0.1;
        
        // Update video if the difference is noticeable
        if (Math.abs(targetTime - currentTime) > 0.001) {
            video.currentTime = currentTime;
        }
        
        requestAnimationFrame(updateVideoTime);
    };
    
    // Start the loop once metadata (duration) is loaded
    video.addEventListener('loadedmetadata', () => {
        requestAnimationFrame(updateVideoTime);
    });
    
    // Fallback in case metadata is already loaded before event listener attaches
    if (video.readyState >= 1) {
         requestAnimationFrame(updateVideoTime);
    }
});

// star-rating.js

document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating i');
    const ratingInput = document.getElementById('selectedRating');

    stars.forEach(star => {
        star.addEventListener('click', () => {
            const ratingValue = star.getAttribute('data-rating');
            ratingInput.value = ratingValue;
            updateStars(ratingValue);
        });

        star.addEventListener('mouseover', () => {
            const ratingValue = star.getAttribute('data-rating');
            updateStars(ratingValue);
        });

        star.addEventListener('mouseout', () => {
            const currentRating = ratingInput.value;
            updateStars(currentRating);
        });
    });

    function updateStars(rating) {
        stars.forEach(star => {
            const starValue = star.getAttribute('data-rating');
            star.classList.toggle('active', starValue <= rating);
        });
    }
});

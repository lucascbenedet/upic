document.addEventListener('DOMContentLoaded', function () {
    var gallery = document.querySelector('.image-grid');
    var getVal = function (elem, style) { return parseInt(window.getComputedStyle(elem).getPropertyValue(style)); };
    var getHeight = function (item) { return item.querySelector('.content').getBoundingClientRect().height; };
    var resizeAll = function () {
        var altura = getVal(gallery, 'grid-auto-rows');
        var gap = getVal(gallery, 'grid-row-gap');
        gallery.querySelectorAll('.image-container').forEach(function (item) {
            var el = item;
            el.style.gridRowEnd = "span " + Math.ceil((getHeight(item) + gap) / (altura + gap));
        });
    };

    gallery.querySelectorAll('.image-container').forEach(function (item) {
        var image = item.querySelector('.gallery-image');
        var likeButton = item.querySelector('.like-heart');
        var commentsSection = item.querySelector('.comments');
        var commentInput = item.querySelector('.comment-field');
        var submitBtn = item.querySelector('.button-comment');

        image.addEventListener('click', function () {
            item.classList.toggle('full');
            document.body.classList.toggle('blurred-background'); //desfoque
        });

        likeButton.addEventListener('click', function () {
            var imageId = image.getAttribute('data-image-id');
        });

        commentInput.addEventListener('input', function () {
            var comment = commentInput.value;
        });

        submitBtn.addEventListener('click', function () {
            var imageId = image.getAttribute('data-image-id');
            var comment = commentInput.value;
        });
    });

    window.addEventListener('resize', resizeAll);
});

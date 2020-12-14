// TODO: Write JS to enlarge an image and center it when the image is clicked
// Intent: On click, the image will enlarge to fit 80% (subject to change) of the viewport's height
// It will be centered in the viewport and the background will be darkened
// The original image will stay in the same place at the same size

$('img.small').click(function() {
    $(this).after('<img class="large" src="' + $(this).attr('src') + '" alt="ENLARGED IMAGE">');
});

$('img.large').click(function() {
    $(this).remove();
});

$('.download-card').click(function () {
    html2canvas($('#download')[0], {scale:5}).then(function(canvas) {
        return Canvas2Image.saveAsPNG(canvas);
    });  
});
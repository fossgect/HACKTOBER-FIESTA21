let list = $(".list");

function anim() {
    let st = list.scrollTop()+list.height();
    let sb = list.prop("scrollHeight");
    let diff = sb - st;
    if(diff <= 1 & diff >= -1) {
        list.animate({scrollTop: 0}, 0, "linear", anim);
    }
    else {
        list.animate({scrollTop: sb}, (sb-st)*15, "linear", anim);
    }
}

anim();

list.mouseenter(
    function() {
        list.stop();
    }
);

list.mouseleave(
    function() {
        anim();
    }
);
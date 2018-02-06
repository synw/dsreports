var w = window,
    d = document,
    e = d.documentElement,
    g = d.getElementsByTagName('body')[0],
    windowHeight = w.innerHeight|| e.clientHeight|| g.clientHeight;
var headerHeight = document.getElementById('header').offsetHeight;
var ban = document.getElementById('banner');
var res = windowHeight-headerHeight;
h = res+"px";
windowWidth = w.innerWidth|| e.clientWidth|| g.clientWidth;
if (windowWidth > 940) {
	ban.style.height = h;
}

function toggleMenu() {
	var menu = document.getElementById("menu");
	if (menu.classList.contains('is-active')) {
		menu.classList.remove("is-active");
	} else {
		menu.classList.add("is-active");
	}
	
}

function fullHeight() {
	if (windowWidth < 941) {
		return
	}
	var bans = document.getElementsByClassName("is-full-height");
	h = windowHeight+"px";
	for (i=0;i<bans.length;i++) {
		bans[i].style.height = h;
	}
}

fullHeight()

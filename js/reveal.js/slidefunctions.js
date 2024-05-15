
    Reveal.initialize({
                        controls: true,
                        progress: false,
                        history: true,
                        center: false,
                        
                        slideNumber: 'c/t' ,
                        math: {
                        mathjax: '../js/MathJax-2.7.7/MathJax.js',
                        config: 'TeX-AMS_HTML-full'  // See http://docs.mathjax.org/en/latest/config-files.html
                        },
                       menu: {
									markers: true,
									openSlideNumber: true,
									keyboard: false,
									themes: [
										{ name: 'Black', theme: '../js/reveal.js/theme/black.css' },
										{ name: 'White', theme: '../js/reveal.js/theme/white.css' },
										{ name: 'League', theme: '../js/reveal.js/theme/league.css' },
										{ name: 'Sky', theme: '../js/reveal.js/theme/sky.css' },
										{ name: 'Beige', theme: '../js/reveal.js/theme/beige.css' },
										{ name: 'Simple', theme: '../js/reveal.js/theme/simple.css' },
										{ name: 'Serif', theme: '../js/reveal.js/theme/serif.css' },
										{ name: 'Blood', theme: '../js/reveal.js/theme/blood.css' },
										{ name: 'Night', theme: '../js/reveal.js/theme/night.css' },
										{ name: 'Moon', theme: '../js/reveal.js/theme/moon.css' },
										{ name: 'Solarized', theme: '../js/reveal.js/theme/solarized.css' }
										],
										custom: [
										{ title: 'Code Style', icon: '<i class="fa fa-external-link">', src: '../js/reveal.js/codeThemes.html' },
										]
			        
                                    },
            // Optional libraries used to extend on reveal.js
            dependencies: [
                            { src: '../js/reveal.js/libjs/classList.js', condition: function() { return !document.body.classList; } },
                            { src: '../js/reveal.js/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                            { src: '../js/reveal.js/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                            { src: '../js/reveal.js/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                            { src: '../js/reveal.js/plugin/math/math.js', async: true },
                            { src: '../js/reveal.js/plugin/menu/menu.js' },
                            { src: '../js/reveal.js/plugin/line-numbers/line-numbers.js'},
                            { src:'../js/reveal.js/plugin/reveal-sampler/sampler.js' },
                            { src:'../js/reveal.js/reveal.js-fullscreen-code.js' },
                            { src: '../js/reveal-plantuml.min.js' },
                            ],

    });
    var gCurrentSlide=0;
    Reveal.addEventListener( 'slidechanged', function( event ) {

		
  	var totalslides = document.querySelectorAll( '.reveal .slides section:not(.stack)' ).length;
  	var current_slide = 0;

  	var horizontal_slides = document.querySelectorAll( '.reveal .slides>section' );
  	for (var i = 0; i < event.indexh; i++)
		 {
    // get subslides
    	var subslides = horizontal_slides[i].querySelectorAll('section');

    // if subslides.length is 0, add 1 for horizontal slide, else add subslides.length
    	current_slide += (subslides.length === 0) ? 1 : subslides.length;
  	}

  	current_slide += event.indexv+1;
		gCurrentSlide=current_slide;
		//console.log("slide "+gCurrentSlide);

    // event.previousSlide, event.currentSlide, event.indexh, event.indexv
} );

function loadCss(name){

var head = document.getElementsByTagName('head')[0],
   link = document.createElement('link');
   link.type = 'text/css';
   link.rel = 'stylesheet';
   link.href = "js/reveal.js/lib/css/"+name;
   head.appendChild(link);


    console.log(name);
    return link;
}

// note I assume that the folder will always be lectureNN so we search for that

function processURLForHome(name , w)
{

    w = w || window;
    var rx = new RegExp('[\&|\?]'+name+'=([^\&\#]+)'),
        val = w.location.search.match(rx);
    return !val ? '':val[1];
}


function goHome()
{
    var location=processURLForHome('home');
    console.log('home is '+location);
    if(location == '')
    {
      var url=window.location.href;
      var n = url.indexOf("slides");
      var home=url.substring(0,n)
      document.location.href=home;
    }
    else{
      document.location.href=location;
    }

}
// 3. On Reveal.js ready event, copy header/footer <div> into each `.slide-background` <div>
var header = $('#header').html();
if ( window.location.search.match( /print-pdf/gi ) ) {
    Reveal.addEventListener( 'ready', function( event ) {
        $('.slide-background').append(header);
    });
}
else {
    $('div.reveal').append(header);
}


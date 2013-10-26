(function(){
	var _Map = {

		initMap: function(domId) {

			if (document.getElementById(domId)) {
				var map = L.mapbox.map(domId, 'nickelmu.map-2dw8613j');

			}
		}
	}


	window.BEY = $.extend(window.BEY || {}, {Map: _Map});



	$(function(){
		window.BEY.Map.initMap('map');
	});

})();

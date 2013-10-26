(function(){
	var _Map = {

		initMap: function() {
			var map = _Map.map = L.mapbox.map('map', 'examples.map-9ijuk24y');
			var geolocate = _Map.geolocate = document.getElementById('geolocate');


			// This uses the HTML5 geolocation API, which is available on
			// most mobile browsers and modern browsers, but not in Internet Explorer
			//
			// See this chart of compatibility for details:
			// http://caniuse.com/#feat=geolocation
			if (!navigator.geolocation) {
			    geolocate.innerHTML = 'geolocation is not available';
			} else {
			    geolocate.onclick = Map.locateMap(e);
			};

			_Map.listen();
		},

		locateMap: function (e) {
	        e.preventDefault();
	        e.stopPropagation();
			_Map.map.locate();
		},

		// Event listeners
		listen: function() {
			var map = _Map.map,
				geolocate = _Map.geolocate;

			// Once we've got a position, zoom and center the map
			// on it, and add a single marker.
			map.on('locationfound', _Map.onLocationFound);

			// If the user chooses not to allow their location
			// to be shared, display an error message.
			map.on('locationerror', _Map.onLocationError);
		},

		onLocationFound: function(e) {
			var map = _Map.map,
				geolocate = _Map.geolocate;

		    map.fitBounds(e.bounds);
		    map.setZoom(14);

		    map.markerLayer.setGeoJSON({
		        type: "Feature",
		        geometry: {
		            type: "Point",
		            coordinates: [e.latlng.lng, e.latlng.lat]
		        },
		        properties: {
		            'marker-color': '#000',
		            'marker-symbol': 'star-stroked'
		        }
		    });

		    // And hide the geolocation button
		    geolocate.parentNode.removeChild(geolocate);


		    console.log('hey we found youuuu');
		},

		onLocationError: function() {
		    _Map.geolocate.innerHTML = 'position could not be found';
		}
	};



	window.BEY = $.extend(window.BEY || {}, {Map: _Map});



	$(function(){
		console.log('docready');
		window.BEY.Map.initMap();
	});

})();

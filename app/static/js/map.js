(function(){
	var _Map = {

		initMap: function() {
			if (! $('#map').length ) {return}

			var map = _Map.map = L.mapbox.map('map', 'examples.map-9ijuk24y');
			var geolocate = _Map.geolocate = document.getElementById('geolocate'),
				$geolocate = _Map.$g = $(geolocate);


			// This uses the HTML5 geolocation API, which is available on
			// most mobile browsers and modern browsers, but not in Internet Explorer
			//
			// See this chart of compatibility for details:
			// http://caniuse.com/#feat=geolocation
			if (!navigator.geolocation) {
			    geolocate.innerHTML = 'geolocation is not available';
			} else {
			    // geolocate.onclick = _Map.locateMap(e);
			    $geolocate.on('click', _Map.locateMap)
			};

			_Map.listen();
		},

		locateMap: function (e) {
			var $g = _Map.$g;

	        e.preventDefault();
	        e.stopPropagation();
	        // _Map.geolocate.
			_Map.map.locate();
			$g.text('Locating');
			BEY.Util.appendSpinner($g);
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


		    console.log('hey we found youuuu');
		    console.log(e);


		    // Post to the server!
		    $.ajax({
		        url: '/store_location',
		        data: {
		            latitude: e.latitude,
		            longitude: e.longitude
		        },
		        type: 'POST',
		        dataType: 'json'
		    })
		    .done(function(data){
		        // pop up your friends' locations??
		        // ie server should return nearby friends' lat/long pairs; js will render
		        console.log('success');
		        console.log(data);
		    });

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

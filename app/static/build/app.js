(function(){
	var _Util = {
		SPINNER_SRC: '/static/image/spinner.gif',

		appendSpinner: function($target) {
			$target = $target || $('body');

			var $spin = $('<img src=' + _Util.SPINNER_SRC + ' class="spinner" />');

			$target.append($spin);

		}
	};



	window.BEY = $.extend(window.BEY || {}, {Util: _Util});


})();

(function(){
	var B = {
		handleAuthResponseChange: function(initialResponse){
			var authResponse = initialResponse.authResponse,
				userObj = {
					status: initialResponse.status,
					userID: authResponse.userID,
					accessToken: authResponse.accessToken,
					expiresIn: authResponse.expiresIn
				};

			$.when.apply(window, [
				BEY.getBasicInfo(userObj),
				BEY.getFriendList(userObj)
			]).then(function(data){
				BEY.postLogin(userObj);
			});

		},

		// Facebook get basic info request
		getBasicInfo: function(baseObj) {
			var infoPromise = $.Deferred();

			FB.api('/me?fields=id,name,picture', function(response) {
				$.extend(baseObj, response);
				infoPromise.resolve(baseObj);
			});

			return infoPromise.promise();
		},


		getFriendList: function(baseObj) {
			var friendsPromise = $.Deferred();

			FB.api('/me/friends', function(response) {
				$.extend(baseObj, {friends: response});
				friendsPromise.resolve(baseObj);
			});

			return friendsPromise.promise()
		},

		postLogin: function(data) {
			console.log('what is the data obj we are sending');
			console.log(data);
			console.log(data.user);

			$.ajax({
				url: '/login',
				data: data,
				dataType: 'JSON',
				type: 'POST'
			})
			.done(function(data){
				console.log('yeahhhhh logged in. redirect to prompt things????');
				window.location.href = '/map';
			})
			.fail(function(){
				console.log('couldn\'t log you in to our server :((((');
			})

		}
	}


	window.BEY = $.extend(window.BEY || {}, B);
})();
window.fbAsyncInit = function() {
  // init the FB JS SDK
  FB.init({
    appId      : '464331713686340',                        // App ID from the app dashboard
    channelUrl : 'http://localhost:5000/static/channel.html', // Channel file for x-domain comms
    status     : true,
    cookie     : true,                                 // Check Facebook Login status
    xfbml      : true                                  // Look for social plugins on the page
  });

  // Additional initialization code such as adding Event Listeners goes here
  FB.Event.subscribe('auth.authResponseChange', function(response) {
    // Here we specify what we do with the response anytime this event occurs. 
    if (response.status === 'connected') {
      // The response object is returned with a status field that lets the app know the current
      // login status of the person. In this case, we're handling the situation where they 
      // have logged in to the app.
      // testAPI();
      BEY.handleAuthResponseChange(response);
    } else if (response.status === 'not_authorized') {
      // In this case, the person is logged into Facebook, but not into the app, so we call
      // FB.login() to prompt them to do so. 
      // In real-life usage, you wouldn't want to immediately prompt someone to login 
      // like this, for two reasons:
      // (1) JavaScript created popup windows are blocked by most browsers unless they 
      // result from direct interaction from people using the app (such as a mouse click)
      // (2) it is a bad experience to be continually prompted to login upon page load.
      FB.login();
    } else {
      // In this case, the person is not logged into Facebook, so we call the login() 
      // function to prompt them to do so. Note that at this stage there is no indication
      // of whether they are logged into the app. If they aren't then they'll see the Login
      // dialog right after they log in to Facebook. 
      // The same caveats as above apply to the FB.login() call here.
      FB.login();
    }
  });
};
(function(){
	var _Map = {

		initMap: function() {
			if (! $('#map').length ) {return};

			var map = _Map.map = L.mapbox.map('map', 'examples.map-9ijuk24y');

			if ($('body').hasClass('landing')) {return};
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

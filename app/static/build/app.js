(function(){
	var BEY = {
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
				window.location.href = '/success';
			})
			.fail(function(){
				console.log('couldn\'t log you in to our server :((((');
			})

		}
	}


	return window.BEY = BEY;
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
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

			$.when([
				BEY.getBasicInfo(userObj),
				BEY.getFriendList(userObj)
			]).then(function(data){
				console.log('got both responses!');
				console.log(userObj);

				BEY.postLogin(userObj);
			});

		},

		// Facebook get basic info request
		getBasicInfo: function(baseObj) {
			var infoPromise = $.Deferred();

			FB.api('/me?fields=id,name,picture', function(response) {
				$.extend(baseObj, {user: response});
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
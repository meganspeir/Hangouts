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

var vidTube = angular.module("vidTube", ['infinite-scroll'])

// The default API base url
.constant('baseurl', 'http://192.168.1.105:8000')

vidTube.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});
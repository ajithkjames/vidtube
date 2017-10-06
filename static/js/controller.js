
vidTube.controller("homeController", function ($scope, Video) {

  $scope.video = new Video();

   });

vidTube.factory('Video', function($http) {
  var Video = function() {
    this.items = [];
    this.busy = false;
    this.after = '';
    this.url = "http://127.0.0.1:8000/api/videos/";
  };

  Video.prototype.nextPage = function() {
    if (this.busy) return;
    this.busy = true;
    $http.get(this.url).then(function successCallback(response)  {
      var items = response.data.results;
      console.log(items)
      for (var i = 0; i < items.length; i++) {
        this.items.push(items[i]);
      }
      this.after = "?page=" + 2;
      this.url = response.data.next;
      if (this.url != null){
        this.busy = false;
        console.log("haiii")
      }

    }.bind(this));
  };

  return Video;
});
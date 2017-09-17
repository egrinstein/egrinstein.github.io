
var fetchPlot = function(){
	$('code#plotgen').html("Loading...")
    $.ajax({
	    url:'http://plot-generator.herokuapp.com',
	    type:'GET',
	    timeout:2000,
	    success: function(data){
	    	$('code#plotgen').html(data["text"]);
	    },
	    error: function(data){
	    	$('code#plotgen').html("Failed to fetch plot.");
    	}
    });
}

$(document).ready( function(){

     fetchPlot();
     $('button#plotgen').on('click', function () {
        fetchPlot();
    });
     
})


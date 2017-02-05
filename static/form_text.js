$(document).ready(function() {
    
    $('form').on('submit', function(event) {
        event.preventDefault();
        
        //Call REST
        $.ajax({
               type : 'POST',
               url : '/allcomment',
               dataType : 'html',
               data : { textInput : $('#textInput').val(),
                        userName : $('#userName').val()
               }
        })
        .done(function(data) {
              var responseJson = $.parseJSON(data);
              var allPosts = '';
              
              //Loop in all comments
              $(responseJson.posts).each(function(index, value) {
                  allPosts = allPosts + '<b>' + value.username + '</b> - ' +
                                         value.datetime + '<BR>' +
                                         value.text + '<BR><BR>';
              });
              
              //Return content to the page
              //$('#alltexts').text(allPosts).show();
              $('#alltexts').html(allPosts).show();
        });
    });
});
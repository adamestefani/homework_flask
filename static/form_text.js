$(document).ready(function() {
    
    $('form').on('submit', function(event) {
        event.preventDefault();
        
        $.ajax({
               type : 'POST',
               url : '/allcomment',
               dataType : 'html',
               data : { textInput : $('#textInput').val() }
        })
        .done(function(data) {
              var responseJson = $.parseJSON(data);
              
              $('#alltexts').text(responseJson.text).show();
        });
    });
});
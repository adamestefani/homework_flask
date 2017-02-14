$(document).on('click', '.send-reply-comment', function(event){    
    
    //Get postid (father id)
    var currentPostId = event.target.id;
    
    //Validate data
    var currentTextInput = $('#textInput'+currentPostId).val();
    var currentUserName = $('#userName'+currentPostId).val();
    var currentPostId = $('#postId'+currentPostId).val();
    var currentCityInput = $('#cityInput'+currentPostId).val();
    var missingField = '';
    var errorField = '';


    if (currentCityInput == ''){
        missingField = '#cityInput'+currentPostId;
        errorField = 'city';
    }
    if (currentTextInput == ''){
        missingField = '#textInput'+currentPostId;
        errorField = 'message';
    }
    if (currentUserName == ''){
        missingField = '#userName'+currentPostId;
        errorField = 'user name';
    }
    
    if (missingField == ''){
        
        //Call REST
        $.ajax({
               type : 'POST',
               url : '/allcomment',
               dataType : 'html',
               data : { textInput : $('#textInput'+currentPostId).val(),
                        userName : $('#userName'+currentPostId).val(),
                        parentId : $('#postId'+currentPostId).val(),
                        city : $('#cityInput'+currentPostId).val()
               }
        })
        .done(function(data) {
              var responseJson = $.parseJSON(data);
              var allPosts = '';
              var previousTextLevel = 0;
              var new_item = '';
              var arrayPost = [];
              
              //Loop in all comments
              $(responseJson.posts).each(function(index, value) {
                  
                  //Verify control variable - previous text level
                  if (previousTextLevel == 0) {
                      previousTextLevel = value.textlevel;
                  };

                  //Create indentation
                  if (previousTextLevel < value.textlevel) {
                      new_item = new_item + '<ul style="list-style-type:none">';
                  }

                  //Close indentation
                  if (previousTextLevel > value.textlevel) {
                      for (i=0;i < (previousTextLevel - value.textlevel); i++) {
                          new_item = new_item + '</ul>';
                      }
                  }

                  //Verify current post level == original post AND if there is an item
                  if (value.textlevel == 1 && new_item) {

                      //Close item tag
                      new_item = new_item + '</li><br>';

                      //Add item to array
                      arrayPost.push(new_item);
                      
                      //New item body
                      new_item = '';
                  }

                  var degree = String.fromCharCode(176);

                  //Populate posts
                  new_item = new_item + '<li>' +
                      '<b>' + value.username + '</b> - ' +
                      value.city +
                      ' (' + value.latitude + degree + ' N, ' + 
                      value.longitude + degree + ' W' + 
                      ') - Weather: ' + value.temperature + degree + ' C - ' +
                      value.datetime + '<br>' +
                      value.text + '<br>' +
                        '<div class="childPost">' +
                          '<input type="hidden" id="postId'+value.postid+'" name="postId" class="postId" value="'+value.postid+'">' +
                          '<input type="text" id="userName'+value.postid+'" name="userName" placeholder="User Name">' +
                          '<input type="text" id="textInput'+value.postid+'" name="textInput" placeholder="Your Message">' +
                          '<input type="text" id="cityInput'+value.postid+'" name="cityInput" placeholder="Your City">' +
                          '<input type="button" value="Done" id="'+value.postid+'" class="send-reply-comment">' +
                        '</div>';

                  //Update control variable
                  previousTextLevel = value.textlevel;
              });
              
              //Verify last post: Close indentation
              if (previousTextLevel > 1) {
                  for (i=0;i < (previousTextLevel - 1); i++) {
                      new_item = new_item + '</ul>';
                  }
              }

              //Verify last post: if there is an item
              if (new_item) {

                  //Close item tag
                  new_item = new_item + '</li><br>';

                  //Add item to array
                  arrayPost.push(new_item);
              }

              //Populate posts from newest to older
              for (i=arrayPost.length; i>0; i--) {
                  allPosts = allPosts + arrayPost[i-1];
              }

              //Return content to the page
              $("#commentItems").html(allPosts);
              $('#alltexts').show();
              
              //Reset fields
              $('#textInput'+currentPostId).val('');
              $('#userName'+currentPostId).val('');
              $('#cityInput'+currentPostId).val('');
        });
    }
    else {
      //Show error message
      alert('Please inform your '+errorField);

      //Focus on missing field
      $(missingField).focus();
    }
});


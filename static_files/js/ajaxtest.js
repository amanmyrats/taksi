// $(document).ready(
//     function(){
//         console.log( "ready!" );
//         $("#test").click(function(){
//         console.log( "clicked" );
//         });

        
    $("#isde").click(
        function(){
            console.log("clicked inside ajaxtest")

            $.ajax({
                // data: $(this).serialize(), // get the form data
                url: "http://127.0.0.1:8000/get/ajax/statuschange/",
                type: 'get',
                data: {
                    status: $(this).val()
                },
                success: function(response){
                    console.log(response);
                    $("#status").text(response.new_status);
                },
            });
        },
    );


    $("#dyncda").click(
        function(){
            console.log("clicked inside ajaxtest")

            $.ajax({
                // data: $(this).serialize(), // get the form data
                url: "http://127.0.0.1:8000/get/ajax/statuschange/",
                type: 'get',
                data: {
                    status: $(this).val()
                },
                success: function(response){
                    console.log(response);
                    $("#status").text(response.new_status);
                },
            });
        },
    );
//     }
//   );
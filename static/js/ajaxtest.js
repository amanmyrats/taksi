// $(document).ready(
//     function(){
//         console.log( "ready!" );
//         $("#test").click(function(){
//         console.log( "clicked" );
//         });

        
    $("input[type=radio][name=work]").change(
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
                    this.text(response.new_status);
                },
            });
        },
    );

//     }
//   );
$('#showButton').click(
    function() {
        $('#hidden').slideDown();
    });
 
$('#hideButton').click(
    function() {
        $('#hidden').slideUp();
    });

$('#sidebarButton').click(
    function() {
        $(".box-1, .box-3, .box-4").animate({"margin-left": '10em'});
        $(this).attr("disabled", true);
        $('#hideSidebarButton').removeAttr("disabled");
    });

$('#hideSidebarButton').click(
    function() {
        $(".box-1, .box-3, .box-4").animate({"margin-left": '-=10em'});
        $('#sidebarButton').removeAttr("disabled");
        $(this).attr("disabled", true);
    });
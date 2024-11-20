document.getElementById('navigate').addEventListener('click', function(){
    const condition=true;
    if(condition){
        window.location.href="{{url_for('registration_page')}}"
    }
    else{
        window.location.href="{{url_for('prediction_page_1')}}}"
    }
});
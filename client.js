$(document).ready(() => {

	let socket = io.connect('http://127.0.0.1:5000');

	socket.on('connect', () => {
		socket.send('Anonymous User has connected!');
	});

	socket.on('message', (msg) => {
		$("#messages").append('<li>'+msg+'</li>');
		console.log('Received message');
	});

	$('#sendbutton').on('click', () => {
		socket.send($('#myMessage').val());
		$('#myMessage').val('');
	});

});
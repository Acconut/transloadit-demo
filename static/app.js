var uppy = Uppy.Core({
	debug: true,
	autoProceed: false
})

uppy.use(Uppy.Dashboard, {
	target: '#uppy-container',
	inline: true
})
uppy.use(Uppy.Transloadit, {
	service: 'https://api2.transloadit.com',
	params: {
		auth: {
			key: "YOUR_AUTH_KEY"
		},
		template_id: "YOUR_TEMPLATE_ID",
	},
	waitForEncoding: true
})

uppy.on('transloadit:complete', (assembly) => {
	fetch('/add_uploads', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(assembly)
	}).then(res => location.reload());
})

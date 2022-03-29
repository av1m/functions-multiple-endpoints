def entrypoint(app, request):
    # Create a new app context for the app
    internal_ctx = app.test_request_context(
        path=request.full_path, method=request.method
    )
    # Copy the request headers to the app context
    internal_ctx.request = request
    # Activate the context
    internal_ctx.push()
    # Dispatch the request to the internal app and get the result
    return_value = app.full_dispatch_request()
    # Offload the context
    internal_ctx.pop()
    # Return the result of the internal app routing and processing
    return return_value

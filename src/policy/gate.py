class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    image = str(body.get("image", ""))
    if image.endswith(":latest") or image == "latest":
        failed.append("image_tag_latest")

    if body.get("privileged"): failed.append("privileged")
    return {"passed": not failed, "failed": failed, "applied": False}

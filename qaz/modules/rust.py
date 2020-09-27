from qaz.modules.asdf import ASDFModule


class Rust(ASDFModule):
    """A programming language focused on performance and safety, especially safe concurrency."""

    name = "Rust"
    plugin_name = "rust"
    vscode_extensions = [
        "rust-lang.rust",
    ]

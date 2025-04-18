class Layout_widgets:
    def __init__(self):
        pass

    def layout_widgets(container):
        # Layout the widgets
        container.label_widget.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        container.progressbar_widget.grid(
            row=1, column=0, padx=30, pady=30, columnspan=2, sticky="ew"
        )
        container.entry_widget.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
        container.checkbox_widget.grid(row=3, column=3, padx=10, pady=10, sticky="e")
        container.submit_widget.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        container.remove_widget.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        container.listbox_widget.grid(row=5, column=0, padx=20, pady=20, columnspan=3, sticky="ew")
        container.browsefile_widget.grid(row=4, column=0, padx=10, pady=10)
        container.my_text_widget.grid(row=4, column=1, padx=10, pady=10, sticky="w")

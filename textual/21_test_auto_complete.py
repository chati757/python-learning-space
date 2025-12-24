from textual.app import App, ComposeResult
from textual.content import Content
from textual.widgets import Input, Label
from textual_autocomplete import AutoComplete, DropdownItem

# Languages with their popularity rank
LANGUAGES_WITH_RANK = [
    (1, "Python"),
    (2, "JavaScript"),
    (3, "Java"),
    (4, "C++"),
    (5, "TypeScript"),
    (6, "Go"),
    (7, "Ruby"),
    (8, "Rust"),
]

# Create dropdown items with styled rank in prefix
CANDIDATES = [
    DropdownItem(
        language,  # Main text to be completed
        prefix=Content.from_markup(
            f"[$text-primary on $primary-muted] {rank:>2} "
        ),  # Prefix with styled rank
    )
    for rank, language in LANGUAGES_WITH_RANK
]

class LanguageSearcher(App):
    CSS="""
    AutoComplete {
        /* Customize the dropdown */
        & AutoCompleteList {
            max-height: 6;  /* The number of lines before scrollbars appear */
            color: $text-primary;  /* The color of the text */
            background: $primary-muted;  /* The background color of the dropdown */
            border-left: wide $success;  /* The color of the left border */
        }

        /* Customize the matching substring highlighting */
        & .autocomplete--highlight-match {
            color: $text-accent;
            text-style: bold;
        }

        /* Customize the text the cursor is over */
        & .option-list--option-highlighted {
            color: $text-success;
            background: $error 50%;  /* 50% opacity, blending into background */
            /*text-style: italic; */
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Start typing a programming language:")
        text_input = Input(placeholder="Type here...<press_down to view list>")
        yield text_input
        yield AutoComplete(target=text_input, candidates=CANDIDATES)
        yield Label("Start typing a programming language:")

if __name__ == "__main__":
    app = LanguageSearcher()
    app.run()
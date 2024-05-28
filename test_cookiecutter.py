"""Test the template generation."""

# %% IMPORTS

from pytest_cookies.plugin import Cookies

# %% TESTS
def test_bake_project(cookies):
    """Test the generation of the project."""
    # given
    extra_context = {
        "project_long_name": "My Project",
        "project_name_dashes": "my-project",
        "project_name_underscores": "my_project"
    }

    # when
    result = cookies.bake(extra_context=extra_context)

    # then
    # project_path = f'{extra_context["project_name_dashes"]}'
    # then
    assert result.exit_code == 0
    assert result.exception is None
    #assert result.project_path.is_dir()
    #assert result.project_path.name == project_path
  
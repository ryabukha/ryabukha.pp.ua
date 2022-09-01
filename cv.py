import yaml
import sys
import os


from weasyprint import HTML, CSS

def load_cv():
    with open("cv.yaml", "r") as stream:
        try:
            cv_data = yaml.safe_load(stream)
            return cv_data
        except yaml.YAMLError as exc:
            print(exc)
CV_DATA = load_cv()

def render_pdf(
    source_html_file="./output/cvfull.html",
    output_file="./output/cvfull.pdf"
):

    html = HTML(source_html_file)
    css = CSS(string='''
        .print-hidden {
            display: none;
        }
        '''
    )

    html.write_pdf(
        output_file, stylesheets=[css])

if __name__ == "__main__":
    source_html_file = os.path.join(sys.argv[1], "cvfull.html")
    output_file = os.path.join(sys.argv[1], "cvfull.pdf")
    render_pdf(source_html_file=source_html_file,
        output_file=output_file)
    print("ok")

#CSS styling
sekcss = """
<style>

.rendered_html
{
  font-size: 140%;
  line-height: 1.1;
  margin: 0.5em 0;
  }

.title
{
  font-size: 250%;
  font-weight:bold;
  line-height: 1.2; 
  margin: 10px 50px 10px;
  }

.subtitle
{
  font-size: 180%;
  font-weight:bold;
  line-height: 1.2; 
  margin: 20px 50px 20px;
  }

.slide-header, p.slide-header
{
  font-size: 200%;
  font-weight:bold;
  margin: 0px 20px 10px;
  page-break-before: always;
  text-align: center;
  }

.rendered_html h1
{
  color: #00628B;
  line-height: 1.2; 
  margin: 0.15em 0em 0.5em;
  page-break-before: always;
  text-align: center;
  }

.rendered_html h2
{ 
  color: #81A594;
  line-height: 1.2;
  margin: 1.1em 0em 0.5em;
  }

.rendered_html h3
{
  color:  #333330; 
  font-size: 120%;
  line-height: 1.2;
  margin: 1.1em 0em 0.5em;
  }

.rendered_html li
{
  line-height: 1.8;
}

.input_prompt, .CodeMirror-lines, .output_area
{
  font-family: Consolas;
  font-size: 100%;
  }

.gap-above
{
  padding-top: 200px;
}

.gap01
{
  padding-top: 10px;
  }

.gap05
{
  padding-top: 50px;
  }

.gap1
{
  padding-top: 100px;
  }

.gap2
{
  padding-top: 200px;
  }

.gap3
{
  padding-top: 300px;
  }

#.emph
#{
#  color: #386BBC;
#  }

.warn
{
  color: red;
  }

.center
{
  text-align: center;
  }

.nb_link
{
    padding-bottom: 0.5em;
}

body{   font-family: "Lucida Grande", "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;  
   color: #333330;
   background-color: #EBEBEA;
}

.rendered_html body{
   font-family: "Lucida Grande", "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif;   
   color: #333330;
   background-color: #EBEBEA;
}
.rendered_html code {
   color: #333330;
   background-color: #EBEBEA;
}
</style>"""
from IPython.display import display, HTML
display(HTML(sekcss))

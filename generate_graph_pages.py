#!/usr/bin/env python3
"""
Generate all 371 graph detail pages for the Angular Rigidity project.
Each page will be named Graph_{i}_pg.html where i is from 0 to 370.
"""

import os

# HTML template for each graph page
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Angular Rigidity - Graph {graph_num}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        
        .nav-link {{
            display: inline-block;
            margin-bottom: 20px;
            padding: 8px 16px;
            background-color: #0066cc;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-size: 14px;
            transition: background-color 0.2s;
        }}
        
        .nav-link:hover {{
            background-color: #0052a3;
        }}
        
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }}
        
        .graph-image-container {{
            text-align: center;
            margin: 30px 0;
        }}
        
        .graph-image-container img {{
            max-width: 100%;
            height: auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            background-color: #f9f9f9;
            padding: 10px;
        }}
        
        .graph-details {{
            margin-top: 30px;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }}
        
        .graph-details p {{
            margin: 10px 0;
            font-size: 14px;
        }}
        
        .navigation {{
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
            gap: 10px;
        }}
        
        .nav-button {{
            padding: 8px 16px;
            background-color: #0066cc;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.2s;
            text-align: center;
        }}
        
        .nav-button:hover {{
            background-color: #0052a3;
        }}
        
        .nav-button.disabled {{
            background-color: #ccc;
            cursor: not-allowed;
            pointer-events: none;
        }}
    </style>
</head>
<body>
    <a href="graphs.html" class="nav-link">← Back to Gallery</a>
    
    <div class="container">
        <h1>Graph {graph_num}</h1>
        
        <div class="graph-image-container">
            <img src="Graph_{graph_num}.png" alt="Graph {graph_num}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22400%22 height=%22300%22%3E%3Crect width=%22100%25%22 height=%22100%25%22 fill=%22%23f9f9f9%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22%23999%22 font-family=%22Arial, Helvetica, sans-serif%22 font-size=%2214%22%3EImage not available%3C/text%3E%3C/svg%3E'">
        </div>
        
        <div class="graph-details">
            <h2>Graph Properties</h2>
            <p><strong>Graph Number:</strong> {graph_num}</p>
            <p><strong>Vertices:</strong> 5</p>
            <p><strong>Chromatic Polynomial:</strong> 4-colored</p>
            <p><strong>Category:</strong> 5-Vertex Graphs with Angular Rigidity</p>
        </div>
        
        <div class="navigation">
            {prev_button}
            <a href="graphs.html" class="nav-button">View All Graphs</a>
            {next_button}
        </div>
    </div>
</body>
</html>'''

def generate_all_pages(output_dir='.'):
    """
    Generate all 371 graph pages.
    
    Args:
        output_dir: Directory where pages will be saved (default: current directory)
    """
    
    total_graphs = 371
    
    for i in range(total_graphs):
        # Create previous button
        if i > 0:
            prev_button = f'<a href="Graph_{i-1}_pg.html" class="nav-button">← Previous</a>'
        else:
            prev_button = '<span class="nav-button disabled">← Previous</span>'
        
        # Create next button
        if i < total_graphs - 1:
            next_button = f'<a href="Graph_{i+1}_pg.html" class="nav-button">Next →</a>'
        else:
            next_button = '<span class="nav-button disabled">Next →</span>'
        
        # Format the HTML
        html_content = HTML_TEMPLATE.format(
            graph_num=i,
            prev_button=prev_button,
            next_button=next_button
        )
        
        # Create filename
        filename = f'Graph_{i}_pg.html'
        filepath = os.path.join(output_dir, filename)
        
        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Print progress
        if (i + 1) % 50 == 0:
            print(f'Created {i + 1}/{total_graphs} pages...')
    
    print(f'✓ Successfully created all {total_graphs} graph pages!')

if __name__ == '__main__':
    generate_all_pages()

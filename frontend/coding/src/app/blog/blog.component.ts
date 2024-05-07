import { Component, OnInit } from '@angular/core';
import { BlogService } from '../blog.service'; 

@Component({
  selector: 'app-blog-list',
  templateUrl: './blog.component.html',
  styleUrls: ['./blog.component.css']
})
export class BlogListComponent implements OnInit {
  blogs = [];

  constructor(private blogService: BlogService) { }

  ngOnInit(): void {
    this.blogService.getBlogs().subscribe(data => {
      this.blogs = data;
    });
  }
}

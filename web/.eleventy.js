const { DateTime } = require("luxon");
const markdownItAnchor = require("markdown-it-anchor");

const pluginRss = require("@11ty/eleventy-plugin-rss");
const pluginSyntaxHighlight = require("@11ty/eleventy-plugin-syntaxhighlight");
const pluginBundle = require("@11ty/eleventy-plugin-bundle");
const pluginNavigation = require("@11ty/eleventy-navigation");
const { EleventyHtmlBasePlugin } = require("@11ty/eleventy");
const sectionizePlugin = require("./_plugins/eleventy-plugin-sectionize");

module.exports = function (eleventyConfig) {
	// Define htmlDateString filter
	eleventyConfig.addFilter("htmlDateString", (dateObj) => {
		return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("yyyy-MM-dd");
	});

	// Define readableDate filter
	eleventyConfig.addFilter("readableDate", (dateObj) => {
		return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("MMMM dd, yyyy");
	});

	// Define filterTagList filter
	eleventyConfig.addFilter("filterTagList", function (tags) {
		if (!tags) return [];
		return tags.filter(tag => !["all", "nav", "post", "posts"].includes(tag));
	});

	// Define slugify filter
	eleventyConfig.addFilter("slugify", function (tag) {
		return tag.toString().toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
	});

	// Copy the contents of the `public` folder to wp-content to emulate WordPress behavior.
	eleventyConfig.addPassthroughCopy({
		"./public/": "/wp-content/"
	});
	// image passthrough
	eleventyConfig.addPassthroughCopy("**/*.{png,jpg,jpeg,gif,svg,webp}");
	// yml passthrough
	eleventyConfig.addPassthroughCopy("**/*.yml");
	// Admin index.html passthrough
	eleventyConfig.addPassthroughCopy("admin/index.html");

	// Exclude the admin folder from processing
	eleventyConfig.ignores.add("admin/index.html");

	// Passthrough for admin/index.html to ensure it is copied
	eleventyConfig.addPassthroughCopy({
		"admin/index.html": "admin/index.html"
	});

	eleventyConfig.addPlugin(sectionizePlugin);
	eleventyConfig.addTemplateFormats("md");

	// note at the moment Nunjucks (njk) file are being parsed as Liquid (liquid) files
	// this results in a number of errors when using Nunjucks specific syntax.
	// For now, I'm using Liquid syntax in the Nunjucks files to avoid these errors.
};

function Span(el)
  if el.t == 'Span' then
    for i, content in ipairs(el.content) do
      if content.t == 'Str' and content.text == "x" then
        -- Replace it with an HTML checkbox (checked)
        el.content[i] = pandoc.RawInline('html', '<input type="checkbox">')
      end
    end
  end
  return el
end

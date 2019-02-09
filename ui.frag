#version 330 core

out vec4 FragColor;

//in vec3 uiColor;
in vec2 texCoord;

uniform sampler2D uiTexture;
uniform sampler2D uiTextureFace;

void main()
{
    FragColor = mix(texture(uiTexture, texCoord), texture(uiTextureFace, texCoord), 0.2);// * vec4(uiColor, 1.0);
}
